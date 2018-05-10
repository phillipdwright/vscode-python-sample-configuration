from random import Random

from args import create_argument_parser
from trees import NodeFactory, TreeBuilder, TreeTraverser

def main():
    argument_parser = create_argument_parser()
    args = argument_parser.parse_args()

    child_count, lower_bound, upper_bound, levels = map(
        int, (args.child_count, args.lower_bound, args.upper_bound, args.levels)
    )
    
    tree = create_tree(child_count, lower_bound, upper_bound, levels)
    max_row_sum = find_max_row_sum(tree)

    message = 'Maximum row sum of {sum} occurs on row {row}'.format(
        row=max_row_sum.row_number,
        sum=max_row_sum.sum
    )
    print(message)

def create_tree(child_count, lower_bound, upper_bound, levels):
    rng = Random()

    node_factory = NodeFactory(rng)
    node_factory.lower_bound = lower_bound
    node_factory.upper_bound = upper_bound

    tree_builder = TreeBuilder(node_factory)
    tree_builder.children_per_node = child_count
    tree_builder.levels = levels

    return tree_builder.build()

def find_max_row_sum(tree):
    traverser = TreeTraverser()
    return traverser.find_maximum_row_sum(tree)

if __name__ == '__main__':
    main()
