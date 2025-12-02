# Etherscan Supported Chains Reference

## Dynamic Chain List Endpoint

Etherscan provides a `/v2/chainlist` endpoint to fetch the current list of all supported chains:

```bash
curl -s "https://api.etherscan.io/v2/api?chainid=1&module=proxy&action=chainlist&apikey=$ETHERSCAN_API_KEY"
```

Use this endpoint to get the most up-to-date chain support information.

## Major Mainnets (Free Tier Available)

| Chain            | Chain ID | Notes         |
| ---------------- | -------- | ------------- |
| Ethereum Mainnet | `1`      | Default chain |
| Polygon Mainnet  | `137`    |               |
| Arbitrum One     | `42161`  |               |
| Arbitrum Nova    | `42170`  |               |
| Linea Mainnet    | `59144`  |               |
| Scroll Mainnet   | `534352` |               |
| zkSync Mainnet   | `324`    |               |
| Mantle Mainnet   | `5000`   |               |
| Blast Mainnet    | `81457`  |               |
| Moonbeam         | `1284`   |               |
| Moonriver        | `1285`   |               |
| Gnosis           | `100`    |               |
| Celo             | `42220`  |               |
| Fraxtal          | `252`    |               |

## Free Tier NOT Available

The following chains require a paid Etherscan plan:

| Chain             | Chain ID |
| ----------------- | -------- |
| Base Mainnet      | `8453`   |
| OP Mainnet        | `10`     |
| Avalanche C-Chain | `43114`  |
| BNB Smart Chain   | `56`     |

## Other Mainnets

| Chain            | Chain ID |
| ---------------- | -------- |
| Abstract         | `2741`   |
| ApeChain         | `33139`  |
| Berachain        | `80094`  |
| BitTorrent Chain | `199`    |
| HyperEVM         | `999`    |
| Katana           | `747474` |
| Monad            | `143`    |
| opBNB            | `204`    |
| Sei              | `1329`   |
| Sonic            | `146`    |
| Swellchain       | `1923`   |
| Taiko            | `167000` |
| Unichain         | `130`    |
| World            | `480`    |
| XDC              | `50`     |

## Testnets

| Chain              | Chain ID    |
| ------------------ | ----------- |
| Sepolia            | `11155111`  |
| Holesky            | `17000`     |
| Hoodi              | `560048`    |
| Abstract Sepolia   | `11124`     |
| ApeChain Curtis    | `33111`     |
| Arbitrum Sepolia   | `421614`    |
| Berachain Bepolia  | `80069`     |
| BitTorrent Testnet | `1029`      |
| Blast Sepolia      | `168587773` |
| Celo Sepolia       | `11142220`  |
| Fraxtal Hoodi      | `2523`      |
| Linea Sepolia      | `59141`     |
| Mantle Sepolia     | `5003`      |
| Moonbase Alpha     | `1287`      |
| Polygon Amoy       | `80002`     |
| Scroll Sepolia     | `534351`    |
| Sei Testnet        | `1328`      |
| Sonic Testnet      | `14601`     |
| Swellchain Testnet | `1924`      |
| Taiko Hoodi        | `167013`    |
| Unichain Sepolia   | `1301`      |
| World Sepolia      | `4801`      |
| XDC Apothem        | `51`        |
| zkSync Sepolia     | `300`       |
