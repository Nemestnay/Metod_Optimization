import sympy as sym
import xlsxwriter
import random

g1 = random.uniform(0, 1)
g2 = (1 - g1 ** 2) ** 0.5
mas = [random.uniform(-5, 5),random.uniform(-10, 10)]
print('A, B:',mas)
print('g1, g2:', g1, g2)
A = mas[0]
B = mas[1]
def f1(dannie, a, b, g1, g2, gamma):
    otvet = 0
    for i in range(len(dannie)):
        x = dannie[i][0]
        y = dannie[i][1]
        otvet += sym.expand(((a + gamma * g1)* x + b + gamma * g2 - y) ** 2)
    return otvet


def fi1(gamma):
    global A, B, g1, g2
    return f1(dannie, A, B, g1, g2, gamma)


def f2(dannie, a, b, g1, g2, gamma):
    otvet = 0
    for i in range(len(dannie)):
        x = dannie[i][0]
        y = dannie[i][1]
        otvet += sym.expand(abs((a + gamma * g1)* x + b + gamma * g2 - y))
    return otvet



def fi2(gamma):
    global A, B, g1, g2
    return f2(dannie, A, B, g1, g2, gamma)


dannie = [[1, 0], [2, -1], [3, -3], [4, 2], [5, -2]]
eps = 0.000001
delta = eps / 4
workbook = xlsxwriter.Workbook('table1.xlsx')


def dihotomia_fi1():
    a = -10
    b = 10
    c = (a + b) / 2 - delta
    d = (a + b) / 2 + delta
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 10, 'Дихотомия φ1')
    worksheet.write(0, 0, 'n')
    worksheet.write(0, 1, 'An')
    worksheet.write(0, 2, 'Bn')
    worksheet.write(0, 3, 'εn=(Bn - An) / 2')
    worksheet.write(0, 4, 'Cn')
    worksheet.write(0, 5, 'Dn')
    worksheet.write(0, 6, 'φ1(Cn)')
    worksheet.write(0, 7, 'φ1(Dn)')
    worksheet.write(1, 0, '0')
    worksheet.write(1, 1, a)
    worksheet.write(1, 2, b)
    worksheet.write(1, 3, (b - a) / 2)
    worksheet.write(1, 4, c)
    worksheet.write(1, 5, d)
    worksheet.write(1, 6, fi1(c))
    worksheet.write(1, 7, fi1(d))
    i = 2
    while abs(b - a) > 2 * eps:
        if fi1(c) >= fi1(d):
            a = c
        else:
            b = d
        c = (a + b) / 2 - delta
        d = (a + b) / 2 + delta
        worksheet.write(i, 0, i - 1)
        worksheet.write(i, 1, '%.8f' % a)
        worksheet.write(i, 2, '%.8f' % b)
        worksheet.write(i, 3, '%.8f' % ((b + a) / 2))
        worksheet.write(i, 4, '%.8f' % c)
        worksheet.write(i, 5, '%.8f' % d)
        worksheet.write(i, 6, '%.8f' % (fi1(c)))
        worksheet.write(i, 7, '%.8f' % (fi1(d)))
        i += 1
    worksheet.write(2, 10, 'Точка минимума:')
    worksheet.write(3, 10, '%.8f' % ((c + d) / 2))
    worksheet.write(4, 10, 'Значение:')
    worksheet.write(5, 10, '%.8f' % fi1((c + d) / 2))
    worksheet.write(2, 13, 'Уравнение:')
    worksheet.write(3, 13, 'y = '+ str('%.3f' % A) + '* x + '+ str('%.3f' % B))


def dihotomia_fi2():
    a = -10
    b = 10
    c = (a + b) / 2 - delta
    d = (a + b) / 2 + delta
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 10, 'Дихотомия φ2')
    worksheet.write(0, 0, 'n')
    worksheet.write(0, 1, 'An')
    worksheet.write(0, 2, 'Bn')
    worksheet.write(0, 3, 'εn=(Bn - An) / 2')
    worksheet.write(0, 4, 'Cn')
    worksheet.write(0, 5, 'Dn')
    worksheet.write(0, 6, 'φ2(Cn)')
    worksheet.write(0, 7, 'φ2(Dn)')
    worksheet.write(1, 0, '0')
    worksheet.write(1, 1, a)
    worksheet.write(1, 2, b)
    worksheet.write(1, 3, (b - a) / 2)
    worksheet.write(1, 4, c)
    worksheet.write(1, 5, d)
    worksheet.write(1, 6, fi2(c))
    worksheet.write(1, 7, fi2(d))
    i = 2
    while abs(b - a) > 2 * eps:
        if fi2(c) >= fi2(d):
            a = c
        else:
            b = d
        c = (a + b) / 2 - delta
        d = (a + b) / 2 + delta
        worksheet.write(i, 0, i - 1)
        worksheet.write(i, 1, '%.8f' % a)
        worksheet.write(i, 2, '%.8f' % b)
        worksheet.write(i, 3, '%.8f' % ((b - a) / 2))
        worksheet.write(i, 4, '%.8f' % c)
        worksheet.write(i, 5, '%.8f' % d)
        worksheet.write(i, 6, '%.8f' % (fi2(c)))
        worksheet.write(i, 7, '%.8f' % (fi2(d)))
        i += 1
    worksheet.write(2, 10, 'Точка минимума:')
    worksheet.write(3, 10, '%.8f' % ((c + d) / 2))
    worksheet.write(4, 10, 'Значение:')
    worksheet.write(5, 10, '%.8f' % fi2((c + d) / 2))
    worksheet.write(2, 13, 'Уравнение:')
    worksheet.write(3, 13, 'y = '+ str('%.3f' % A) + '* x + '+ str('%.3f' % B))


def zolotoe_sechenie_fi1():
    a = -10
    b = 10
    c = a + ((3 - 5 ** 0.5) * (b - a)) / 2
    d = a + ((5 ** 0.5 - 1) * (b - a)) / 2
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 10, 'Золотое сечение φ1')
    worksheet.write(0, 0, 'n')
    worksheet.write(0, 1, 'An')
    worksheet.write(0, 2, 'Bn')
    worksheet.write(0, 3, 'εn=(Bn - An) / 2')
    worksheet.write(0, 4, 'Cn')
    worksheet.write(0, 5, 'Dn')
    worksheet.write(0, 6, 'φ1(Cn)')
    worksheet.write(0, 7, 'φ1(Dn)')
    worksheet.write(1, 0, '0')
    worksheet.write(1, 1, a)
    worksheet.write(1, 2, b)
    worksheet.write(1, 3, (b - a) / 2)
    worksheet.write(1, 4, c)
    worksheet.write(1, 5, d)
    worksheet.write(1, 6, fi1(c))
    worksheet.write(1, 7, fi1(d))
    i = 2
    while abs(b - a) > 2 * eps:
        if fi1(c) >= fi1(d):
            a = c
            c = d
            d = a + ((5 ** 0.5 - 1) * (b - a)) / 2
        else:
            b = d
            d = c
            c = a + ((3 - 5 ** 0.5) * (b - a)) / 2
        worksheet.write(i, 0, i - 1)
        worksheet.write(i, 1, '%.8f' % a)
        worksheet.write(i, 2, '%.8f' % b)
        worksheet.write(i, 3, '%.8f' % ((b + a) / 2))
        worksheet.write(i, 4, '%.8f' % c)
        worksheet.write(i, 5, '%.8f' % d)
        worksheet.write(i, 6, '%.8f' % (fi1(c)))
        worksheet.write(i, 7, '%.8f' % (fi1(d)))
        i += 1
    worksheet.write(2, 10, 'Точка минимума:')
    worksheet.write(3, 10, '%.8f' % ((c + d) / 2))
    worksheet.write(4, 10, 'Значение:')
    worksheet.write(5, 10, '%.8f' % fi1((c + d) / 2))
    worksheet.write(2, 13, 'Уравнение:')
    worksheet.write(3, 13, 'y = '+ str('%.3f' % A) + '* x + '+ str('%.3f' % B))


def zolotoe_sechenie_fi2():
    a = -10
    b = 10
    c = a + ((3 - 5 ** 0.5) * (b - a)) / 2
    d = a + ((5 ** 0.5 - 1) * (b - a)) / 2
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 10, 'Золотое сечение φ2')
    worksheet.write(0, 0, 'n')
    worksheet.write(0, 1, 'An')
    worksheet.write(0, 2, 'Bn')
    worksheet.write(0, 3, 'εn=(Bn - An) / 2')
    worksheet.write(0, 4, 'Cn')
    worksheet.write(0, 5, 'Dn')
    worksheet.write(0, 6, 'φ2(Cn)')
    worksheet.write(0, 7, 'φ2(Dn)')
    worksheet.write(1, 0, '0')
    worksheet.write(1, 1, a)
    worksheet.write(1, 2, b)
    worksheet.write(1, 3, (b - a) / 2)
    worksheet.write(1, 4, c)
    worksheet.write(1, 5, d)
    worksheet.write(1, 6, fi2(c))
    worksheet.write(1, 7, fi2(d))
    i = 2
    while abs(b - a) > 2 * eps:
        if fi2(c) >= fi2(d):
            a = c
            c = d
            d = a + ((5 ** 0.5 - 1) * (b - a)) / 2
        else:
            b = d
            d = c
            c = a + ((3 - 5 ** 0.5) * (b - a)) / 2


        worksheet.write(i, 0, i - 1)
        worksheet.write(i, 1, '%.8f' % a)
        worksheet.write(i, 2, '%.8f' % b)
        worksheet.write(i, 3, '%.8f' % ((b + a) / 2))
        worksheet.write(i, 4, '%.8f' % c)
        worksheet.write(i, 5, '%.8f' % d)
        worksheet.write(i, 6, '%.8f' % (fi2(c)))
        worksheet.write(i, 7, '%.8f' % (fi2(d)))
        i += 1
    worksheet.write(2, 10, 'Точка минимума:')
    worksheet.write(3, 10, '%.8f' % ((c + d) / 2))
    worksheet.write(4, 10, 'Значение:')
    worksheet.write(5, 10, '%.8f' % fi2((c + d) / 2))
    worksheet.write(2, 13, 'Уравнение:')
    worksheet.write(3, 13, 'y = '+ str('%.3f' % A) + '* x + '+ str('%.3f' % B))




dihotomia_fi1()
dihotomia_fi2()
zolotoe_sechenie_fi1()
zolotoe_sechenie_fi2()

workbook.close()

