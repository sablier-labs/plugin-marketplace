# Critical Rules for Effect-TS

These rules are **non-negotiable**. Violations will cause runtime errors or break Effect's type safety.

## FORBIDDEN: try-catch in Effect.gen

**Never use `try-catch` blocks inside `Effect.gen` generators.**

Effect generators handle errors through the Effect type system, not JavaScript exceptions. Using try-catch will cause
runtime errors and break Effect's error handling.

**Wrong:**

```typescript
Effect.gen(function* () {
  try {
    const result = yield* someEffect;
  } catch (error) {
    // This will never be reached and breaks Effect semantics
  }
});
```

**Correct:**

```typescript
Effect.gen(function* () {
  const result = yield* Effect.result(someEffect);
  if (result._tag === "Failure") {
    // Handle error case
  }
});
```

Alternative patterns:

- `Effect.catchAll` / `Effect.catchTag` for error recovery
- `Effect.result` to inspect success/failure
- `Effect.tryPromise` / `Effect.try` for wrapping external code

## FORBIDDEN: Type Assertions

**Never use `as never`, `as any`, or `as unknown` type assertions.**

These break TypeScript's type safety and hide real type errors. Always fix the underlying type issues.

**Forbidden patterns:**

```typescript
const value = something as any;
const value = something as never;
const value = something as unknown;
```

**Correct approach:**

- Use proper generic type parameters
- Import correct types from Effect
- Use proper Effect constructors and combinators
- Adjust function signatures to match usage

## MANDATORY: return `yield*` for Errors

**Always use `return yield*` when yielding errors or interrupts in Effect.gen.**

This makes it clear that the generator function terminates at that point.

**Correct:**

```typescript
Effect.gen(function* () {
  if (someCondition) {
    return yield* Effect.fail("error message");
  }

  if (shouldInterrupt) {
    return yield* Effect.interrupt;
  }

  const result = yield* someOtherEffect;
  return result;
});
```

**Wrong:**

```typescript
Effect.gen(function* () {
  if (someCondition) {
    yield* Effect.fail("error message");
    // Unreachable code after error - confusing and error-prone
  }
});
```

The `return` keyword makes termination explicit and prevents unreachable code.
