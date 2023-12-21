import re

class Polynomial:
    def __init__(self, polynomial):
        self.polynomial = polynomial

    def derivative(self):
        # 使用正则表达式拆分多项式为单项式
        terms = re.findall(r'([+-]?[0-9]*[a-z](?:\^\d+)?)', self.polynomial)
        derivative_terms = []

        for term in terms:
            # 解析单项式以获取系数、变量和指数
            coef, var, exp = self.parse_term(term)

            # 处理常数项（幂指数为0）
            if exp == 0:
                continue

            # 计算导数的系数和指数
            new_coef = coef * exp
            new_exp = exp - 1

            # 构建导数表达式
            if new_exp == 0:
                derivative_terms.append(f"{new_coef:+}")
            else:
                derivative_terms.append(f"{new_coef:+}{var}" + (f"^{new_exp}" if new_exp != 1 else ""))

        # 格式化和拼接导数表达式
        # 将导数项列表合并成一个字符串，项与项之间用空格隔开
        derivative_expression = ' '.join(derivative_terms)
        # 将合并后的字符串中的 " + -" 替换为 " - "，这样可以处理减号前的正号问题
        derivative_expression = derivative_expression.replace(' + -', ' - ')
        # 去除字符串最前面的正号（如果有的话）
        derivative_expression = derivative_expression.lstrip('+ ')
        # 去除可能由于去除正号而产生的多余空格
        derivative_expression = derivative_expression.strip()

        return derivative_expression

    def parse_term(self, term):
        # 使用正则表达式提取系数、变量和指数
        match = re.match(r'([+-]?)(\d*)([a-z])(?:\^(\d+))?', term)
        sign = 1 if match.group(1) == '' or match.group(1) == '+' else -1
        coef = int(match.group(2) or '1') * sign
        var = match.group(3)
        exp = int(match.group(4) or '1')
        return coef, var, exp

# Example usage
poly = Polynomial('x^7-x^5+26*x^4+10*x^3-6*x^2-10*x+4')
derivative_result = poly.derivative()
print(f"The derivative is: {derivative_result}")