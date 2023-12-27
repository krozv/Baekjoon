"""
쿼터 25
다임 10
니켈 5
페니 1
거스름돈은 500 cent 이하
동전 개수 최소
"""
import sys
T = int(input())
for i in range(T):
    cent = int(sys.stdin.readline())
    quarter = cent // 25
    rest_cent = cent - quarter * 25
    dime = rest_cent // 10
    rest_cent -= dime * 10
    nickel = rest_cent // 5
    rest_cent -= nickel * 5
    penny = rest_cent
    print(quarter, dime, nickel, penny)