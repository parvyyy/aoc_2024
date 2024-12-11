from collections import defaultdict

def main():
    with open("input.txt", 'r') as f:
        orders = defaultdict(list)

        orderings, updates = f.read().split('\n\n')

        for ordering in orderings.split('\n'):
            target, predecessor = ordering.split('|')
            target, predecessor = int(target), int(predecessor)
            
            orders[target].append(predecessor)

        sum = 0
        for update in updates.split('\n'):
            update = [int(u) for u in update.split(',')]
            middle_page_no = update[int((len(update) - 1) / 2)]

            # Create a mapping for page to position
            page_to_position = dict()
            for (i, v) in enumerate(update):
                page_to_position[v] = i

            valid_update = True

            for page in update:
                # For all the 'orderings' of the given page,
                # ensure that they are BEHIND all others in the
                # 'order' list.
                for v in orders[page]:
                    # If predecessor not in list, skip!
                    if v not in page_to_position:
                        continue
                    
                    # Wrong order!
                    if page_to_position[v] < page_to_position[page]:
                        valid_update = False

            if valid_update:
                sum += middle_page_no

        print(sum)

if __name__ == "__main__":
    main()