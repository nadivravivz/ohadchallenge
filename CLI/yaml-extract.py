import argparse
from argparse import RawTextHelpFormatter
import yaml
import json
from jsonpath_ng import jsonpath, parse
import sys


parser = argparse.ArgumentParser(description='Tool that extracts a value from a YAML text based on a path expression', formatter_class=RawTextHelpFormatter)
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
required.add_argument('-f','--file', help='\nThe name of a yaml file.\nIf the file name is `-`, then it is read from stdin', required=True,)
required.add_argument('-e','--expr', help='\nThe expression to extract.\nPlease write the expression with double quotes, example: --expr "root.child1.list[0]" ', required=True)
args = parser.parse_args()

try:
    if args.file == "-":
        data = sys.stdin.read()
        json_string = json.dumps(yaml.safe_load(data))
        json_data = json.loads(json_string)
        jsonpath_expression = parse(args.expr)
        match = jsonpath_expression.find(json_data)
        print(match[0].value)

    else:
        with open(args.file) as f:
            json_string = json.dumps(yaml.safe_load(f))
            json_data = json.loads(json_string)
            jsonpath_expression = parse(args.expr)
            match = jsonpath_expression.find(json_data)
            print(match[0].value)

except:
    print("Error with file or expression")
