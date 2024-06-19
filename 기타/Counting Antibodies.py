def calculate_immunoglobulin_variants(V_kappa, J_kappa, V_lambda, J_lambda, V_h, D_h, J_h):
    # 경쇄 조합 계산
    kappa_variants = V_kappa * J_kappa
    lambda_variants = V_lambda * J_lambda
    
    # 중쇄 조합 계산
    heavy_chain_variants = V_h * D_h * J_h
    
    # 총 항체 조합 계산
    total_variants = (kappa_variants + lambda_variants) * heavy_chain_variants
    
    return total_variants

# 입력 받기
V_kappa, J_kappa = map(int, input().split())
V_lambda, J_lambda = map(int, input().split())
V_h, D_h, J_h = map(int, input().split())

# 결과 출력
print(calculate_immunoglobulin_variants(V_kappa, J_kappa, V_lambda, J_lambda, V_h, D_h, J_h))
