# this is actually for extend gro. file for 3-mer P3HT polymer to length I want to simulate.

# define number of units n, so the number of units need to be extended is b
n = 10

# define total number of particles n_particles
n_particles = 4 * n


# 指定文件路径
original_file_path = 'C:/Users/yinfuyin/Desktop/temporary_store/change_3mer_P3HT/modified/CG3mer_gro.txt'
new_file_path = 'C:/Users/yinfuyin/Desktop/temporary_store/change_3mer_P3HT/modified/extend_viaCG3mer_gro.txt'

# 打开文件，使用 'r' 模式表示只读
with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
    for i, line in enumerate(original_file, 1):
        if i == 1:
            # 写入第一行
            new_file.write(line)
        elif i == 2:
            # 修改第二行的'粒子数量'并写入
            new_file.write(str(n_particles) + '\n')
        elif 3 <= i <= 14:
            # 将原文件的第3行至第14行写入新文件：即原始粒子被保留
            new_file.write(line)


# 定义了单元间间隔
delta_x_avg = 0.3225
delta_y_avg = -0.086
delta_z_avg = -0.2155


# 定义了一个关于a的坐标函数
# 偶数单元中，a表示5号CG粒子的类似 b表示6号CG粒子 以此类推。。。c-7 d-8 奇数单元中，e-9 f-10 g-11 h-12
def calculate_ath_particle_coordinates(a):
    x5, y5, z5 = -0.121, 0.001, -0.024
    x_a = x5 + (a - 2) * delta_x_avg
    y_a = y5 + (a - 2) * delta_y_avg
    z_a = z5 + (a - 2) * delta_z_avg
    return x_a, y_a, z_a


def calculate_bth_particle_coordinates(b):
    x6, y6, z6 = -0.165, 0.150, -0.136
    x_b = x6 + (b - 2) * delta_x_avg
    y_b = y6 + (b - 2) * delta_y_avg
    z_b = z6 + (b - 2) * delta_z_avg
    return x_b, y_b, z_b


def calculate_cth_particle_coordinates(c):
    x7, y7, z7 = -0.016, 0.284, -0.264
    x_c = x7 + (c - 2) * delta_x_avg
    y_c = y7 + (c - 2) * delta_y_avg
    z_c = z7 + (c - 2) * delta_z_avg
    return x_c, y_c, z_c


def calculate_dth_particle_coordinates(d):
    x8, y8, z8 = 0.071, 0.584, -0.047
    x_d = x8 + (d - 2) * delta_x_avg
    y_d = y8 + (d - 2) * delta_y_avg
    z_d = z8 + (d - 2) * delta_z_avg
    return x_d, y_d, z_d


def calculate_eth_particle_coordinates(e):
    x9, y9, z9 = 0.187, -0.012, -0.291
    x_e = x9 + (e - 3) * delta_x_avg
    y_e = y9 + (e - 3) * delta_y_avg
    z_e = z9 + (e - 3) * delta_z_avg
    return x_e, y_e, z_e


def calculate_fth_particle_coordinates(f):
    x10, y10, z10 = 0.233, -0.138, -0.155
    x_f = x10 + (f - 3) * delta_x_avg
    y_f = y10 + (f - 3) * delta_y_avg
    z_f = z10 + (f - 3) * delta_z_avg
    return x_f, y_f, z_f


def calculate_gth_particle_coordinates(g):
    x11, y11, z11 = 0.441, -0.221, -0.094
    x_g = x11 + (g - 3) * delta_x_avg
    y_g = y11 + (g - 3) * delta_y_avg
    z_g = z11 + (g - 3) * delta_z_avg
    return x_g, y_g, z_g


def calculate_hth_particle_coordinates(h):
    x12, y12, z12 = 0.749, -0.271, 0.122
    x_h = x12 + (h - 3) * delta_x_avg
    y_h = y12 + (h - 3) * delta_y_avg
    z_h = z12 + (h - 3) * delta_z_avg
    return x_h, y_h, z_h


# 由于我们已经在前面写过 new_file，我们可以重新打开并继续追加它——使用 'a' 模式以追加内容
with open(new_file_path, 'a') as new_file:
    # 对于每个粒子从4遍历到n
    for m in range(4, n+1):
        if m % 2 == 0:  # 检查m是否为偶数
            # 计算类似a粒子的坐标
            x, y, z = calculate_ath_particle_coordinates(m)
            # 将类似a粒子的坐标写入文件
            new_file.write(f"    1MOL    SP1 {4*m-3:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")

            # 计算类似b粒子的坐标
            x, y, z = calculate_bth_particle_coordinates(m)
            # 将类似b粒子的坐标写入文件
            new_file.write(f"    1MOL    SN0 {4*m-2:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")

            # 计算类似c粒子的坐标
            x, y, z = calculate_cth_particle_coordinates(m)
            # 将类似c粒子的坐标写入文件
            new_file.write(f"    1MOL    C05 {4*m-1:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")

            # 计算类似d粒子的坐标
            x, y, z = calculate_dth_particle_coordinates(m)
            # 将类似d粒子的坐标写入文件
            new_file.write(f"    1MOL    C01 {4*m:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")
        else:     # m为奇数
            # 计算类似e粒子的坐标
            x, y, z = calculate_eth_particle_coordinates(m)
            # 将类似e粒子的坐标写入文件
            new_file.write(f"    1MOL    SP1 {4*m-3:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")

            # 计算类似f粒子的坐标
            x, y, z = calculate_fth_particle_coordinates(m)
            # 将类似f粒子的坐标写入文件
            new_file.write(f"    1MOL    SN0 {4*m-2:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")

            # 计算类似g粒子的坐标
            x, y, z = calculate_gth_particle_coordinates(m)
            # 将类似g粒子的坐标写入文件
            new_file.write(f"    1MOL    C05 {4*m-1:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")

            # 计算类似h粒子的坐标
            x, y, z = calculate_hth_particle_coordinates(m)
            # 将类似h粒子的坐标写入文件
            new_file.write(f"    1MOL    C01 {4*m:>4} {x:>7.3f} {y:>7.3f} {z:>7.3f}\n")

# 打开文件，使用 'r' 模式表示只读
with open(original_file_path, 'r') as original_file, open(new_file_path, 'a') as new_file:
    for i, line in enumerate(original_file, 1):
        if i == 15:
            # 写入第一行
            new_file.write(line)


# 然后，读取新文件内容并输出，以检查内容是否合格
with open(new_file_path, 'r') as new_file:
    new_file_content = new_file.read()
    print(new_file_content)
