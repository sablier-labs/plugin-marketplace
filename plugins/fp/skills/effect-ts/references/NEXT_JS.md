# Effect + Next.js Integration

`@mcrovero/effect-nextjs` provides typed helpers for integrating Effect with Next.js 15+ App Router—pages, server
actions, route handlers, and server components.

## Core API

### Creating Handlers

```typescript
import { Next } from "@mcrovero/effect-nextjs";
import { Layer } from "effect";

// Stateless layers (recommended)
const AppLive = Layer.mergeAll(ServiceA.Default, ServiceB.Default);
export const BasePage = Next.make("BasePage", AppLive);

// Stateful layers (database connections, etc.)
import { ManagedRuntime, globalValue } from "effect";
export const runtime = globalValue("AppRuntime", () => {
  const rt = ManagedRuntime.make(StatefulLive);
  process.on("SIGINT", () => rt.dispose());
  return rt;
});
export const BasePage = Next.makeWithRuntime("BasePage", runtime);
```

### Chaining Middleware

```typescript
export const AuthenticatedPage = Next.make("Base", AppLive).middleware(AuthMiddleware).middleware(LoggingMiddleware); // Left-to-right execution
```

### Building Handlers

```typescript
const HomePage = Effect.fn("HomePage")(function* () {
  const user = yield* CurrentUser
  return <div>Hello {user.name}</div>
})

export default BasePage.build(HomePage)
```

## Middleware Definition

Define middleware with `NextMiddleware.Tag()`:

```typescript
import { NextMiddleware } from "@mcrovero/effect-nextjs";
import { Context, Layer, Schema, Effect } from "effect";

// 1. Define the capability tag
export class CurrentUser extends Context.Tag("CurrentUser")<CurrentUser, { id: string; name: string }>() {}

// 2. Define the middleware
export class AuthMiddleware extends NextMiddleware.Tag<AuthMiddleware>()("AuthMiddleware", {
  provides: CurrentUser, // What this middleware provides
  failure: Schema.String // Error type on failure
}) {}

// 3. Implement the middleware
export const AuthMiddlewareLive = Layer.succeed(
  AuthMiddleware,
  AuthMiddleware.of(Effect.fn("AuthMiddleware")(() => Effect.succeed({ id: "1", name: "Ada" })))
);
```

**Middleware options:**

- `provides` - Context.Tag this middleware injects
- `failure` - Schema for error type
- `wrap: true` - Interceptor pattern (run before AND after)
- `catches` - Error types to catch when `wrap: true`
- `returns` - Custom return type when `wrap: true`

## Handler Patterns

```typescript
// Page
export default BasePage.build(pageEffect);

// Server Action
export const myAction = BaseAction.build(actionEffect);

// Route Handler
export const GET = BaseApi.build(getEffect);
export const POST = BaseApi.build(postEffect);

// Server Component (same pattern)
export default BasePage.build(componentEffect);
```

## Utilities

### Navigation

```typescript
import { Redirect, PermanentRedirect, NotFound } from "@mcrovero/effect-nextjs/Navigation";

yield * Redirect("/new-path"); // 307 redirect
yield * PermanentRedirect("/new-path"); // 308 redirect
yield * NotFound; // Render 404
```

### Cache Revalidation

```typescript
import { RevalidatePath, RevalidateTag } from "@mcrovero/effect-nextjs/Cache";

yield * RevalidatePath("/");
yield * RevalidateTag("my-tag");
```

### Request Data

```typescript
import { Headers, Cookies, DraftMode } from "@mcrovero/effect-nextjs/Headers";

const headers = yield * Headers;
const cookies = yield * Cookies;
const draftMode = yield * DraftMode;
```

### Params Decoding

```typescript
import { decodeParamsUnknown, decodeSearchParamsUnknown } from "@mcrovero/effect-nextjs/Params"

const HomePage = Effect.fn("HomePage")(function* (props) {
  const params = yield* decodeParamsUnknown(
    Schema.Struct({ id: Schema.String })
  )(props.params)

  const search = yield* decodeSearchParamsUnknown(
    Schema.Struct({ q: Schema.optional(Schema.String) })
  )(props.searchParams)

  return <div>ID: {params.id}, Query: {search.q}</div>
})
```

## Best Practices

1. **Use `Effect.fn()`** - Automatic telemetry spans and better stack traces
1. **Keep layers stateless** - Use `Next.makeWithRuntime()` + `globalValue` only for stateful services
1. **Centralize base handlers** - Create `BasePage`, `BaseAction`, `BaseApi` with appropriate middleware
1. **Error handling** - Use `.catchAll()` for Effect-level errors, middleware `failure` schema for typed errors
1. **Request caching** - Use `@mcrovero/effect-react-cache` for request-scoped memoization
1. **Skip React hooks** - Effect-ts doesn't benefit client-side hooks; use Effect for server-side code only

______________________________________________________________________

## Implementation Examples

### Service Definition

Define services using `Effect.Service` with methods wrapped in `Effect.fn()`:

```typescript
import { Effect, Schema, Data } from "effect";
import { FileSystem } from "@effect/platform";

// Custom error type
export class TodoError extends Data.TaggedError("TodoError")<{
  message: string;
}> {}

// Service definition
export class TodoStore extends Effect.Service<TodoStore>()("app/TodoStore", {
  effect: Effect.gen(function* () {
    const fs = yield* FileSystem.FileSystem;

    return {
      getAll: Effect.fn("getAll")(function* () {
        const content = yield* fs.readFileString("todos.json");
        return yield* Schema.decodeUnknown(Schema.Array(TodoSchema))(JSON.parse(content));
      }),

      create: Effect.fn("create")(function* (title: string) {
        const todos = yield* this.getAll;
        const newTodo = { id: crypto.randomUUID(), title, done: false };
        yield* fs.writeFileString("todos.json", JSON.stringify([...todos, newTodo]));
        return newTodo;
      })
    };
  })
}) {}
```

### Middleware Implementation

#### Provider Middleware (Non-Wrapped)

```typescript
import { NextMiddleware } from "@mcrovero/effect-nextjs";
import { Context, Layer, Schema, Effect } from "effect";

export class CurrentUser extends Context.Tag("CurrentUser")<CurrentUser, { id: string; name: string }>() {}

export class AuthMiddleware extends NextMiddleware.Tag<AuthMiddleware>()("AuthMiddleware", {
  provides: CurrentUser,
  failure: Schema.String
}) {}

export const AuthMiddlewareLive = Layer.succeed(
  AuthMiddleware,
  AuthMiddleware.of(
    Effect.fn("AuthMiddleware")(() =>
      Effect.gen(function* () {
        // Validate session, fetch user, etc.
        return { id: "user-123", name: "Ada Lovelace" };
      })
    )
  )
);
```

#### Interceptor Middleware (Wrapped)

```typescript
export class LoggingMiddleware extends NextMiddleware.Tag<LoggingMiddleware>()("LoggingMiddleware", { wrap: true }) {}

export const LoggingMiddlewareLive = Layer.succeed(
  LoggingMiddleware,
  LoggingMiddleware.of(({ next }) =>
    Effect.gen(function* () {
      yield* Effect.log("Request started");
      const result = yield* next;
      yield* Effect.log("Request completed");
      return result;
    })
  )
);
```

### Base Layer Configuration

```typescript
import { Next } from "@mcrovero/effect-nextjs";
import { Layer, Logger, LogLevel } from "effect";
import { NodeContext } from "@effect/platform-node";

// Compose all layers
const AppLive = Layer.mergeAll(
  AuthMiddlewareLive,
  LoggingMiddlewareLive,
  TodoStore.Default.pipe(Layer.provide(NodeContext.layer))
).pipe(Layer.provide(Logger.minimumLogLevel(LogLevel.Debug)));

// Create specialized handlers
export const BasePage = Next.make("Base", AppLive).middleware(AuthMiddleware);

export const BaseAction = Next.make("Base", AppLive).middleware(AuthMiddleware);

export const BaseApi = Next.make("Base", AppLive).middleware(LoggingMiddleware).middleware(AuthMiddleware);
```

### Page Example

```typescript
import { Effect, Schema } from "effect"
import { decodeSearchParamsUnknown } from "@mcrovero/effect-nextjs/Params"
import { BasePage, CurrentUser, TodoStore } from "@/lib/base"

const SearchSchema = Schema.Struct({
  q: Schema.optional(Schema.String),
})

const HomePage = Effect.fn("HomePage")(function* (props) {
  const user = yield* CurrentUser
  const { q } = yield* decodeSearchParamsUnknown(SearchSchema)(props.searchParams)
  const todos = yield* TodoStore.pipe(Effect.flatMap((s) => s.getAll))

  const filtered = q ? todos.filter((t) => t.title.includes(q)) : todos

  return (
    <main>
      <h1>Welcome, {user.name}</h1>
      <ul>
        {filtered.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </main>
  )
})

export default BasePage.build(HomePage)
```

### Server Action Example

```typescript
"use server";
import { Effect } from "effect";
import { BaseAction, TodoStore } from "@/lib/base";

const _createTodo = Effect.fn("createTodo")(function* (input: { title: string }) {
  const store = yield* TodoStore;
  const todo = yield* store.create(input.title);
  const todos = yield* store.getAll;
  return { todo, todos, error: null };
}).pipe(Effect.catchAll((err) => Effect.succeed({ todo: null, todos: [], error: err.message })));

export const createTodo = BaseAction.build(_createTodo);
```

### Error Handling Patterns

#### Effect-Level Catch

```typescript
const action = Effect.fn("action")(function* () {
  // ... effect logic
}).pipe(Effect.catchAll((err) => Effect.succeed({ data: null, error: err.message ?? "Unknown error" })));
```

#### Middleware Failure Schema

```typescript
export class AuthMiddleware extends NextMiddleware.Tag<AuthMiddleware>()("AuthMiddleware", {
  provides: CurrentUser,
  failure: Schema.Struct({
    _tag: Schema.Literal("Unauthorized"),
    message: Schema.String
  })
}) {}
```

#### Custom Tagged Errors

```typescript
import { Data } from "effect";

export class NotFoundError extends Data.TaggedError("NotFoundError")<{
  resource: string;
}> {}

export class ValidationError extends Data.TaggedError("ValidationError")<{
  field: string;
  message: string;
}> {}
```

______________________________________________________________________

## Native Effect Platform API Handlers

Build Next.js API handlers directly with `@effect/platform` without wrapper libraries. These patterns complement
`@mcrovero/effect-nextjs` by providing lower-level control.

### Raw HTTP APIs

Use `HttpApp.toWebHandlerRuntime` for simple API handlers with full Effect capabilities.

```typescript
// src/app/api/example/route.ts
import { HttpApp, HttpServerRequest, HttpServerResponse } from "@effect/platform";
import { Effect, Layer, ManagedRuntime, Schema } from "effect";

// Main layer representing all services the handler needs (db, auth, etc.)
const mainLive = Layer.empty;

const managedRuntime = ManagedRuntime.make(mainLive);
const runtime = await managedRuntime.runtime();

// Handler effect consumes request from context and produces HTTP response
const exampleEffectHandler = Effect.gen(function* () {
  // Consume request from context with schema validation
  const { name } = yield* HttpServerRequest.schemaBodyJson(
    Schema.Struct({
      name: Schema.String
    })
  );
  return yield* HttpServerResponse.json({
    message: `Hello, ${name}`
  });
});

const handler = HttpApp.toWebHandlerRuntime(runtime)(exampleEffectHandler);

type Handler = (req: Request) => Promise<Response>;
export const POST: Handler = handler;
```

For most applications, prioritize using the `HttpApi` framework over the `HttpApp` framework. Use `HttpApp` only for
very simple API handlers that don't require a lot of customization.

### Effect HttpApi Framework

Build type-safe APIs with automatic OpenAPI generation, Swagger UI, and client SDK.

#### Schema Definition

Define API groups and endpoints with full type safety:

```typescript
// src/app/api/[[...path]]/route.ts
import {
  FetchHttpClient,
  HttpApi,
  HttpApiBuilder,
  HttpApiClient,
  HttpApiEndpoint,
  HttpApiGroup,
  HttpApiSwagger,
  HttpMiddleware,
  HttpServer,
  OpenApi
} from "@effect/platform";
import { Config, Effect, Layer, Schema } from "effect";

// Custom error type
class FooError extends Schema.TaggedError<FooError>("FooError")("FooError", {}) {}

// API group with endpoints
class FooApi extends HttpApiGroup.make("foo")
  .add(
    HttpApiEndpoint.get("bar", "/bar")
      .setHeaders(Schema.Struct({ page: Schema.NumberFromString }))
      .addSuccess(Schema.String)
  )
  .add(
    HttpApiEndpoint.post("baz", "/baz/:id")
      .setPath(Schema.Struct({ id: Schema.NumberFromString }))
      .setPayload(Schema.Struct({ name: Schema.String }))
      .addSuccess(Schema.Struct({ ok: Schema.Boolean }))
      .addError(FooError)
  ) {}

// Compose API with prefix and OpenAPI metadata
class MyApi extends HttpApi.make("api")
  .add(FooApi)
  .prefix("/api")
  .annotateContext(
    OpenApi.annotations({
      title: "My API",
      description: "API for my endpoints"
    })
  ) {}
```

#### Implementation

Implement handlers with full type inference:

```typescript
const FooLive = HttpApiBuilder.group(MyApi, "foo", (handlers) =>
  handlers
    .handle("bar", (_) => Effect.succeed(`page: ${_.headers.page}`))
    .handle("baz", (_) =>
      Effect.gen(function* () {
        const id = _.path.id;
        if (id < 0) {
          return yield* new FooError();
        }
        return {
          ok: _.payload.name.length === id
        };
      })
    )
);

const ApiLive = HttpApiBuilder.api(MyApi).pipe(Layer.provide(FooLive));
```

#### Middleware Stack

Configure CORS, OpenAPI JSON, Swagger UI, and logging:

```typescript
const middleware = Layer.mergeAll(
  HttpApiBuilder.middlewareCors(),
  HttpApiBuilder.middlewareOpenApi({
    path: "/api/openapi.json"
  }),
  HttpApiSwagger.layer({
    path: "/api/docs"
  }),
  HttpApiBuilder.middleware(HttpMiddleware.logger)
);

const { handler } = Layer.empty.pipe(
  Layer.merge(middleware),
  Layer.provideMerge(ApiLive),
  Layer.merge(HttpServer.layerContext),
  HttpApiBuilder.toWebHandler
);

type Handler = (req: Request) => Promise<Response>;
export const GET: Handler = handler;
export const POST: Handler = handler;
export const PUT: Handler = handler;
export const PATCH: Handler = handler;
export const DELETE: Handler = handler;
export const OPTIONS: Handler = handler;
```

#### Type-Safe Client

Generate a fully typed client from the API schema:

```typescript
const example = Effect.gen(function* () {
  // Import schema only - no runtime dependency
  const client = yield* HttpApiClient.make(MyApi, {
    baseUrl: yield* Config.string("BASE_URL")
  });

  const res = yield* client.foo.bar({ headers: { page: 1 } });
  const res2 = yield* client.foo.baz({
    path: { id: 1 },
    payload: { name: "test" }
  });
  return { res, res2 };
}).pipe(Effect.provide(FetchHttpClient.layer));
```

### waitUntil Pattern

Execute background tasks that continue after the response is sent. Essential for serverless environments.

#### Service Definition

```typescript
import { Effect, Runtime, Context, Layer } from "effect";

class WaitUntil extends Context.Tag("WaitUntil")<WaitUntil, (promise: Promise<unknown>) => void>() {}

const effectWaitUntil = <A, E, R>(effect: Effect.Effect<A, E, R>, abortSignal?: AbortSignal) =>
  Effect.runtime<R>().pipe(
    Effect.zip(WaitUntil),
    Effect.flatMap(([runtime, waitUntil]) =>
      Effect.sync(() => waitUntil(Runtime.runPromise(runtime, effect, { signal: abortSignal })))
    )
  );
```

#### Vercel Integration

```typescript
import { waitUntil } from "@vercel/functions";

const VercelWaitUntil = Layer.succeed(WaitUntil, waitUntil);
```

#### Cloudflare Integration

```typescript
type ExecutionContext = {
  waitUntil(promise: Promise<unknown>): void;
  passThroughOnException(): void;
  props: Record<string, unknown>;
};

const CloudflareWaitUntil = (ctx: ExecutionContext) => Layer.succeed(WaitUntil, ctx.waitUntil);
```
