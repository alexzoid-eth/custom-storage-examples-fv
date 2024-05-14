methods {
    function totalSupply() external returns (uint256) envfree;
}

ghost mathint ghostTotalSupply {
    init_state axiom ghostTotalSupply == 0;
    axiom ghostTotalSupply >= 0 && ghostTotalSupply <= max_uint256;
}

hook Sload uint256 val currentContract.eRC20Storage._totalSupply {
    require(require_uint256(ghostTotalSupply) == val);
}

hook Sstore currentContract.eRC20Storage._totalSupply uint256 val {
    ghostTotalSupply = val;
}
 
rule totalSupplyCheck() {
    assert(ghostTotalSupply == to_mathint(totalSupply()));
}