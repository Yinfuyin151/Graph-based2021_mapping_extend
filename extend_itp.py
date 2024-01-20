# this is actually for extend gro. file for 3-mer P3HT polymer to length I want to simulate.

# define number of units n, so the number of units need to be extended is b
n = 3

# define total number of particles m
m = 4 * n


# 指定文件路径
original_file_path = 'C:/Users/yinfuyin/Desktop/temporary_store/change_3mer_P3HT/modified/3mer_itp.txt'
new_file_path = 'C:/Users/yinfuyin/Desktop/temporary_store/change_3mer_P3HT/modified/extend_viaCG3mer_itp.txt'

# 打开文件，使用 'r' 模式表示只读 w从头写入 a续写
with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
    # 读取前四行内容
    first_few_lines = [original_file.readline() for _ in range(4)]
    # 打开新文件进行写入
    new_file.writelines(first_few_lines)

# 写atoms
# 由于我们已经在前面写过 new_file，我们可以重新打开并继续追加它——使用 'a' 模式以追加内容
with open(new_file_path, 'a') as new_file:
    # 对于每个粒子从4遍历到n
    for i in range(1, m+1):
        line = '{:>5}'.format(f'CG{i}')
        if i % 4 == 1:  # 检查i是否为unit的第 1 个粒子
            # 将类似的内容写入文件
            new_file.write(f"{i:>5}  SP1    1  MOL {line} {i:>4}     0.000    45.000;C:[SH]:C\n")

        elif i % 4 == 2:  # 检查i是否为unit的第 2 个粒子
            # 将类似的内容写入文件
            new_file.write(f"{i:>5}  SN0    1  MOL {line} {i:>4}     0.000    45.000;c1ccccc1\n")

        elif i % 4 == 3:  # 检查i是否为unit的第 3 个粒子
            # 将类似的内容写入文件
            new_file.write(f"{i:>5}  C05    1  MOL {line} {i:>4}     0.000    72.000;CC\n")

        elif i % 4 == 0:  # 检查i是否为unit的第 4 个粒子
            # 将类似的内容写入文件
            new_file.write(f"{i:>5}  C01    1  MOL {line} {i:>4}     0.000    72.000;CCCC\n")


# 写 bonds
# 打开文件，使用 'r' 模式表示只读 w从头写入 a续写
with open(new_file_path, 'a') as new_file:
    # 写入第一行空白
    new_file.write('\n')
    # 写入第二行 "[bonds]"
    new_file.write('[bonds]\n')

    # 对于每个粒子从4遍历到n
    for i in range(1, m+1):
        if i % 4 == 1 and i+4 < m+1:  # 检查i是否为unit的第 1 个粒子
            # 将类似的内容写入文件
            new_file.write(f"{i:>5} {i+4:>2}   1     0.389    1250.0\n")
        elif i % 4 == 2:
            # 将类似的内容写入文件
            new_file.write(f"{i:>5} {i+1:>2}   1     0.235    1250.0\n")
        elif i % 4 == 3:
            # 将类似的内容写入文件
            new_file.write(f"{i:>5} {i+1:>2}   1     0.335    1250.0\n")

# 约束bonds
# 打开文件，使用 'r' 模式表示只读 w从头写入 a续写
with open(new_file_path, 'a') as new_file:
    # 写入第一行空白
    new_file.write('\n')
    # 写入第二行 "#ifdef min"
    new_file.write('#ifdef min\n')

    for i in range(1, m+1):
        if i % 4 == 1:  # 检查i是否为unit的第 1 个粒子
            # 将类似的内容写入文件
            new_file.write(f"{i:>5} {i+1:>2}   1     0.191 5000000.0\n")


# 打开文件，使用 'r' 模式表示只读 w从头写入 a续写
with open(new_file_path, 'a') as new_file:
    # 写入第一行空白
    new_file.write('\n')
    # 写入第二行 "#else"
    new_file.write('#else\n')
    # 写入第三行 "[constraints]"
    new_file.write('[constraints]\n')
    for i in range(1, m+1):
        if i % 4 == 1:  # 检查i是否为unit的第 1 个粒子
            # 将类似的内容写入文件
            new_file.write(f"{i:>5} {i+1:>2}   1     0.191\n")
    # 写入"#endif”
    new_file.write('#endif\n')

# angles
with open(new_file_path, 'a') as new_file:
    # 写入第1行 blank
    new_file.write('\n')
    # 写入第2行 "[angle]"
    new_file.write('[angle]\n')





# 然后，读取新文件内容并输出，以检查内容是否合格
with open(new_file_path, 'r') as new_file:
    new_file_content = new_file.read()
    print(new_file_content)
