from math import sqrt
star37 = [.08342971408, -0.2392481515, -0.4966976975]
star36 = [0.8139832631, -0.5557243189, 0.1691204557]
star35 = [0.4541086270, -0.5392368197, 0.7092312789]
star34 = [0.3201817378, -0.4436021946, -0.8370786986]
star33 = [0.5520184464, -0.7933187400, -0.2567508745]
star32 = [0.4537196908, -0.8779508801, 0.1527766153]
star31 = [0.2069525789, -0.8719885748, -0.4436288486]
star30 = [0.1217293692, -0.7702732847, 0.6259880410]
star29 = [-0.1124304773, -0.9694934200, 0.2178116072]
star28 = [-0.1146237858, -0.3399692557, -0.9334250333]
star27 = [-0.3516499609, -0.8240752703, -0.4441196390]
star26 = [-0.5326876930, -0.7160644554, 0.4511047742]
star25 = [-0.7861763936, -0.5217996305, 0.3311371675]
star24 = [-0.6898393233, -0.4182330640, -0.5909338474]
star23 = [-0.5812035376, -0.2909171294, 0.7599800468]
star22 = [-0.9170097662, -0.3502146628, -0.1908999176]
star21 = [-0.4523440203, -0.0493710140, -0.8904759346]
star20 = [-0.9525211695, -0.0593434796, -0.2986331746]
star19 = [-0.9656605484, 0.0525933156, 0.2544280809]
star18 = [-0.8608205219, 0.4636213989, 0.2098647835]
star17 = [-0.7742591356, 0.6152504197, -0.1482892839]
star16 = [-0.4657947941, 0.4774785033, 0.7450164351]
star15 = [-0.3612508532, 0.5747270840, -0.7342932655]
star14 = [-0.4118589524, 0.9065485360, 0.0924226975]
star13 = [-0.1820751783, 0.9404899869, -0.2869271926]
star12 = [-0.0614937230, 0.6031563286, -0.7952489957]
star11 = [0.1371725575, 0.6813721061, 0.7189685267]
star10 = [0.2011399589, 0.9690337941, -0.1432348512]
star9 = [0.3507315038,0.8926333307,0.2831839492]
star8 = [0.4105636020,4988110001,0.7632988371]
star7 = [0.7032235469,0.7075846047,0.0692868685]
star6 = [0.5450107404,0.5314955466,-0.6484410356]
star5 = [0.0130968840,0.0078062795,0.9998837600]
star4 = [0.4917678276,2204887125,-0.8423473935]
star3 = [0.4775639450,0.1166004340,0.8708254803]
star2 = [0.9342640400,0.1735073142,-0.3115219339]
star1 = [0.8748658918,0.0260879174,0.4836621670]



def findDist(p1,p2):
    dist = sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
    return (dist)

stars = [(star18,star11),(star5,star26),(star25,star5),(star1,star33),(star34,star2),(star18,star25),(star17,star9),(star28,star20),(star34,star6),
(star20,star15),(star36,star34),(star17,star16),(star9,star11),(star28,star12),(star13,star16),(star32,star26),(star29,star30),(star17,star16),(star7,star12),
(star13,star16),(star22,star17),(star11,star18),(star1,star33),(star5,star29)]

liste = []
for i in stars:
    liste.append(findDist(i[0],i[1]))

print(''.join([chr(int(round(i/0.010045))) for i in liste]))