def main():
    def calculate_diversity(n, products, order):

        category_positions = {}
        product_to_category = {product: category for product, category in products}

        for idx, product_id in enumerate(order):
            category = product_to_category[product_id]
            if category not in category_positions:
                category_positions[category] = []
            category_positions[category].append(idx)

        min_diff = float('inf')
        all_unique_categories = True
        for positions in category_positions.values():
            if len(positions) > 1:
                all_unique_categories = False
                positions.sort()
                for i in range(1, len(positions)):
                    diff = positions[i] - positions[i - 1]
                    min_diff = min(min_diff, diff)
        if all_unique_categories:
            return n
        else:
            return min_diff

    n = int(input())
    products = [tuple(map(int, input().split())) for _ in range(n)]
    order = list(map(int, input().split()))

    result = calculate_diversity(n, products, order)

    print(result)


if __name__ == "__main__":
    main()
