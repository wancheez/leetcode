class Solution:
    cache_count_left = {}

    def generateParenthesis(self, n: int) -> list[str]:
        n = n * 2
        results = []
        self.cache_count_left['('] = 1
        results.append('(')
        return self.backtrace(results, n - 1)

    def backtrace(self, variants: list[str], n):
        if n == 0:
            return variants
        new_variants = []
        for variant in variants:
            new_variants.append(variant + '(')
            new_variants.append(variant + ')')
        n -= 1
        new_variants = [variant for variant in new_variants if self.is_valid(variant, n)]
        return [''.join(variant) for variant in self.backtrace(new_variants, n)]

    def is_valid(self, variant: str, left_vals: int):
        last_value = variant[-1]
        old_variant = variant[:len(variant)-1]
        old_count_left = self.cache_count_left[old_variant]
        if last_value == '(':
            count_left = old_count_left + 1
        else:
            count_left = old_count_left
        count_right = len(variant) - count_left

        if count_right > count_left:
            return False

        self.cache_count_left[variant] = count_left
        if count_left - count_right > left_vals:
            return False
        return True


# ["((()))","(()())","(())()","()(())","()()()"]
# '(()))('
print(Solution().generateParenthesis(3))