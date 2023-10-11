import json
import argparse

def convert_postman_to_bruno(input_file, output_file):
    try:
        with open(input_file, 'r') as postman_file:
            postman_data = json.load(postman_file)

        if 'values' in postman_data:
            values = postman_data['values']

            bruno_config = "vars {\n"
            for item in values:
                key = item['key']
                value = item['value']
                bruno_config += f"  {key}: {value}\n"
            bruno_config += "}"

            with open(output_file, 'w') as bruno_file:
                bruno_file.write(bruno_config)
            
            print(f"Conversion completed. Bruno config saved to {output_file}")
        else:
            print("Postman environment file does not have 'values' field.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert Postman environment to Bruno config")
    parser.add_argument("input_file", help="Path to the Postman environment JSON file")
    parser.add_argument("output_file", help="Path to the output Bruno config file")
    args = parser.parse_args()

    convert_postman_to_bruno(args.input_file, args.output_file)
