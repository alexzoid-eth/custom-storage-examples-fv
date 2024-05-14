methods {
    function totalSupply() external returns (uint256) envfree;
    function balanceOf(address account) external returns (uint256) envfree;
}

definition INIT_STORAGE_LOCATION() returns uint256
    = 0x52c63247e1f47db19d5ce0460030c497f067ca4cebf71ba98eeadabe20bace00;

//
// _balances[]
//

// `_balances[]` slot is the same as storage initial slot as it has index 0
definition STORAGE_SLOT_BALANCES() returns uint256 = INIT_STORAGE_LOCATION(); 

definition IS_STORAGE_SLOT_BALANCES_USER(uint256 slot, address user) returns bool 
    = to_bytes32(slot) == keccak256(user, to_bytes32(STORAGE_SLOT_BALANCES())); 

ghost address ghostUser;
ghost mapping (address => mathint) ghostBalanceOf;

//
// _totalSupply
//

definition IS_STORAGE_SLOT_TOTALSUPPLY(uint256 slot) returns bool 
    // 2 - _totalSupply offset 
    = to_bytes32(require_uint256(slot - 2)) == to_bytes32(INIT_STORAGE_LOCATION()); 

ghost mathint ghostTotalSupply;

//
// Global hooks
//

hook ALL_SLOAD(uint256 slot) uint256 val {
    if(IS_STORAGE_SLOT_TOTALSUPPLY(slot)) {
        require(require_uint256(ghostTotalSupply) == val);
    } else if(IS_STORAGE_SLOT_BALANCES_USER(slot, ghostUser)) {
        require(require_uint256(ghostBalanceOf[ghostUser]) == val);
    }
}

hook ALL_SSTORE(uint256 slot, uint256 val)  {
    if(IS_STORAGE_SLOT_TOTALSUPPLY(slot)) {
        ghostTotalSupply = val;
    } else if(IS_STORAGE_SLOT_BALANCES_USER(slot, ghostUser)) {
        ghostBalanceOf[ghostUser] = val;
    }
}

//
// Properties
//

rule totalSupplyCheck() {
    assert(ghostTotalSupply == to_mathint(totalSupply()));
}

rule balanceOfGhostUser() {
    assert(ghostBalanceOf[ghostUser] == to_mathint(balanceOf(ghostUser)));
}