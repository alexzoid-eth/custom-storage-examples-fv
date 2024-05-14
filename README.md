# CVL Custom Storage Location Examples

This repository provides examples of how to interact with and verify the storage when dealing with contracts that encapsulate their storage in a struct accessed via a specific storage slot. These examples are particularly useful for understanding advanced Solidity concepts and Certora's verification language (CVL) for formal verification.

## Overview

The contract `StorageExample` utilizes a structured approach to storage that OpenZeppelin's upgradeable contracts often employ. It defines an `ERC20Storage` struct which is stored in a specific slot determined by a hashing mechanism. The examples show how to access and modify this storage safely and verify these modifications using Certora CVL.

## StorageGap

In the provided example, the `__gap` array size is unusually large, calculated to position the `eRC20Storage` struct at a specific storage location following the gap. This positioning ensures that the struct aligns with an expected storage slot, allowing the contract to safely interact with inherited storage from `StorageExample`. 

```
certoraRun certora/confs/StorageGap.conf
```

https://prover.certora.com/output/52567/58d9f5e5f2994db5bef0796dc22dff12/?anonymousKey=67ed2de0bcd7dd8da01991ca6cf00c2cb2c22a31

## StorageHookAll

Another, quite limited in use approach. In the provided example, the hooks `ALL_SLOAD` and `ALL_SSTORE` are used to intercept and verify all reads (`SLOAD`) and writes (`SSTORE`) to the storage. These hooks are designed to work universally across any storage slot operation.

```
certoraRun certora/confs/StorageHookAll.conf
```

https://prover.certora.com/output/52567/71d13e62394c4f7d8741ba73bf4e8ef3/?anonymousKey=6a0a7c27e2993ab607bfea188248b5cb32e4e15f

## Discussion

[Discussion](https://discord.com/channels/795999272293236746/1238273179760463874) originates from a real question regarding the best way to build a hook around `_balances` in a new OpenZeppelin ERC20 contract format. 