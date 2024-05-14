// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

import {StorageExample} from "../../src/StorageExample.sol";

contract StorageExampleHarness is StorageExample { 
    uint256[37439836327923360225337895871394760624280537466773280374265222508165906222592] private __gap;
    StorageExample.ERC20Storage eRC20Storage; 
}
