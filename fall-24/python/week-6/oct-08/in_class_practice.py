input_file_path = "/home/marlon/studies/fall-24/python/week-6/oct-8/input.txt"
output_file_path = "/home/marlon/studies/fall-24/python/week-6/oct-8/output.txt"

with open(input_file_path, 'r') as input_file:
  content = input_file.read()
  print("Content of the input file:")
  print(content)

with open(output_file_path, 'w') as output_file:
  output_file.write(content)

print(f"\nContent successfully copied to {output_file_path}")


input_file1_path = "/home/marlon/studies/fall-24/python/week-6/oct-8/input1.txt"
input_file2_path = "/home/marlon/studies/fall-24/python/week-6/oct-8/input2.txt"
output_merged_file = "/home/marlon/studies/fall-24/python/week-6/oct-8/merged_output.txt" 

with open(input_file1_path, 'r') as input_file1:
  content1 = input_file1.read()

with open(input_file2_path, 'r') as input_file2:
  content2 = input_file2.read()

with open(output_merged_file, 'w') as output_merged:
  output_merged.write(content1)
  output_merged.write('\n')
  output_merged.write(content2)

print(f'\nContent merged successfully in {output_merged}')
