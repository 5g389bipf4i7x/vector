import numpy as np
import re
import math

'''
    三點一面
    一點一垂直向量
    兩點一平面向量
    兩向量求公垂線方程式
    平行六面體體積(須給3向量)
    點-鏡面點-反射到點(求鏡面方程式)
    兩方程式求法向量
    點面距
'''
#兩點距離
def two_point():
    while True:
        input_pointa = input('請輸入點1的座標(以,或空白分隔): ')
        input_pointb = input('請輸入點2的座標(以,或空白分隔): ')
        try:
            pointa = [int(ipa) for ipa in re.split(r'[\s,]+',input_pointa)]
            pointb = [int(ipb) for ipb in re.split(r'[\s,]+',input_pointb)]
            if len(pointa) != 3 or len(pointb) != 3:
                raise ValueError
            distance = float(distance)
            distance = math.sqrt(((pointa[0]-pointb[0])**2)+((pointa[1]-pointb[1])**2)+((pointa[2]-pointb[2])**2))
            print(distance)
            break
        except (IndexError,ValueError,TypeError):
            print('請檢查輸入值是否正確，是否有包含三軸且使用,或空白鍵分隔')
            continue

#三點求一平面及公垂向量
def three_point():
    while True:
        input_pointa = input("請輸入點1的座標(以,或空白分隔): ")
        input_pointb = input("請輸入點2的座標(以,或空白分隔): ")
        input_pointc = input("請輸入點3的座標(以,或空白分隔): ")
        if input_pointa == input_pointb or input_pointa == input_pointc or input_pointb ==input_pointc:
            print('不可有相同的點\n')
            break
        try:
            pointa = [int(ipa) for ipa in re.split(r'[\s,]+',input_pointa)]
            pointb = [int(ipb) for ipb in re.split(r'[\s,]+',input_pointb)]
            pointc = [int(ipc) for ipc in re.split(r'[\s,]+',input_pointc)]
            vecab = np.array([pointb[0]-pointa[0],pointb[1]-pointa[1],pointb[2]-pointa[2]]) #取得ab向量
            vecac = np.array([pointc[0]-pointa[0],pointc[1]-pointa[1],pointc[2]-pointa[2]]) #取得ac向量
            if len(pointa) != 3 or len(pointb) != 3 or len(pointc) != 3: #檢查輸入值是否少於或多於3個
                raise IndexError
            primaryNabc = (np.cross(vecab,vecac)) #ab、ac向量外積
            if np.array_equal(primaryNabc, [0,0,0]):
                print('三點共線，無法判斷平面')
                break
            if primaryNabc[0] < 0 : #使公垂向量之x為正數
                primaryNabc = -primaryNabc 
            cf3p = math.gcd(int(primaryNabc[0]),int(primaryNabc[1]),int(primaryNabc[2])) #取得公垂向量xyz軸之公因數
            Nabc = primaryNabc/cf3p
            yplus = '+'
            zplus = '+'
            if Nabc[1]< 0 :
                yplus =''
            if Nabc[2]< 0 :
                zplus =''
            print('平面垂直向量為 ('+str(int(Nabc[0]))+','+str(int(Nabc[1]))+','+str(int(Nabc[2]))+')\n平面方程式為 '+
                str(int(Nabc[0]))+'x'+yplus+str(int(Nabc[1]))+'y'+zplus+str(int(Nabc[2]))+'z = '+str(int(Nabc[0]*pointa[0]+Nabc[1]*pointa[1]+Nabc[2]*pointa[2])))
            break
        except (IndexError,ValueError,TypeError):
            print('您輸入的值有誤，請檢查點是否包含三軸且使用,或空白鍵分隔')
            continue


#平面法向量及面上一點
def point_normalvrctor():
    while True:
        input_point = input('請輸入點座標(以,或空白分隔): ')
        input_normal_vector = input('請輸入垂直平面的向量(以,或空白分隔): ')
        try:
            point = [int(ip) for ip in re.split(r'[\s,]+',input_point)]
            n = np.array([int(inv) for inv in re.split(r'[\s,]+',input_normal_vector)])
            if len(point) != 3 or len(n) != 3: #檢查輸入值是否少於或多於3個
                raise IndexError
            if np.array_equal(n,[0,0,0]) :
                print('零向量無法計算平面')
                break
            if n[0] < 0: #使公垂向量之x為正數
                    n = -n
            cfpv = math.gcd(n[0],n[1],n[2]) #取得垂直向量xyz軸之公因數
            Npv = n//cfpv
            yplus = '+'
            zplus = '+'
            if Npv[1]< 0 :
                yplus =''
            if Npv[2]< 0 :
                zplus =''
            print(str(n[0])+'x'+yplus+str(n[1])+'y'+zplus+str(n[2])+'z = '+str(n[0]*point[0]+n[1]*point[1]+n[2]*point[2]))
            break
        except (IndexError,ValueError,TypeError):
            print('您輸入的值有誤，請檢查點和向量有無包含三軸值且使用,或空白鍵分隔')
            continue


#平面上兩點及一向量求平面
def two_point_vector():
    while True:
        input_pointa = input("請輸入點1的座標(以,或空白分隔): ")
        input_pointb = input("請輸入點2的座標(以,或空白分隔): ")
        input_vector = input('請輸入向量的值，以,或空白分隔: ')
        try:
            pointa = [int(ipa) for ipa in re.split(r'[\s,]+', input_pointa)]
            pointb = [int(ipb) for ipb in re.split(r'[\s,]+',input_pointb)]
            vecab = np.array([pointb[0]-pointa[0],pointb[1]-pointa[1],pointb[2]-pointa[2]]) #取得ab向量
            v = np.array([int(iv) for iv in re.split(r'[\s,]+',input_vector)]) #將轉成list(int)的值變成向量值
            if len(pointa) != 3 or len(pointb) != 3 or len(v) != 3:
                raise IndexError
            if np.array_equal(v,[0,0,0]):
                print('零向量無法計算平面')
                break
            if input_pointa == input_pointb:
                print('不可有相同的點\n')
                continue
            primaryNabv = (np.cross(vecab,v))
            if np.array_equal (primaryNabv,[0,0,0]):
                print('此兩點的向量與您提供的向量相同，無法判斷平面')
                break
            if primaryNabv[0] < 0: #使公垂向量之x為正數
                primaryNabv = -primaryNabv
            cf2pv = math.gcd(int(primaryNabv[0]),int(primaryNabv[1]),int(primaryNabv[2]))
            N2pv = primaryNabv/cf2pv
            yplus = '+'
            zplus = '+'
            if N2pv[1]< 0 :
                yplus =''
            if N2pv[2]< 0 :
                zplus =''
            print('平面垂直向量為 ('+str(int(N2pv[0]))+','+str(int(N2pv[1]))+','+str(int(N2pv[2]))+')\n平面方程式為 '+
                str(int(N2pv[0]))+'x'+yplus+str(int(N2pv[1]))+'y'+zplus+str(int(N2pv[2]))+'z = '+str(int(N2pv[0]*pointa[0]+N2pv[1]*pointa[1]+N2pv[2]*pointa[2])))
            break
        except (IndexError,ValueError,TypeError):
            print('您輸入的值有誤，請檢查點和向量有無包含三軸取且使用,或空白鍵分隔')
            continue


#平行四邊形面積
def area_of_parallelongram():
    while True:
        input_veca = input('請輸入a向量(以,或空白鍵分隔): ')
        input_vecb = input('請輸入b向量(以,或空白鍵分隔): ')
        try:
            veca = [int(iva) for iva in re.split(r'[\s,]+',input_veca)]
            vecb = [int(ivb) for ivb in re.split(r'[\s,]+',input_vecb)]
            if len (veca) != 3 or len(vecb) != 3 :
                raise IndexError
            if veca == [0,0,0] or vecb == [0,0,0]:
                print('零向量無法計算面積')
                break
            crossab = np.cross(veca,vecb)
            if np.array_equal(crossab,[0,0,0]):
                print('兩向量平行，無法計算面積')
                break
            area = np.absolute(veca[0]*vecb[1]-veca[1]*vecb[0])/2
            print('面積為: ',area)
            break
        except (IndexError,ValueError,TypeError):
            print('您輸入的向量有誤，請檢查向量是否包含三軸且使用,或空白鍵分隔')
            continue


#三角形面積
def area_of_triangle():
    while True:
        input_veca = input('請輸入a向量(以,或空白鍵分隔): ')
        input_vecb = input('請輸入b向量(以,或空白鍵分隔): ')
        try:
            veca = [int(iva) for iva in re.split(r'[\s,]+',input_veca)]
            vecb = [int(ivb) for ivb in re.split(r'[\s,]+',input_vecb)]
            if len (veca) != 3 or len(vecb) != 3 :
                raise IndexError
            if veca == [0,0,0] or vecb == [0,0,0]:
                print('零向量無法計算面積')
                break
            crossab = np.cross(veca,vecb)
            if np.array_equal(crossab,[0,0,0]):
                print('兩向量平行，無法計算面積')
                break
            area = np.absolute(veca[0]*vecb[1]-veca[1]*vecb[0])/2
            print('三角形面積為: ',area)
            break
        except (IndexError,ValueError,TypeError):
            print('您輸入的向量有誤，請檢查向量是否包含三軸且使用,或空白鍵分隔')
            continue

#平行六面體體積
def volume_of_parallelepiped():
    while True:
        input_veca = input('請輸入a向量(以,或空白分隔): ')
        input_vecb = input('請輸入b向量(以,或空白分隔): ')
        input_vecc = input('請輸入c向量(以,或空白分隔): ')
        try:
            veca = [int(iva) for iva in re.split(r'[\s,]+',input_veca)]
            vecb = [int(ivb) for ivb in re.split(r'[\s,]+',input_vecb)]
            vecc = [int(ivc) for ivc in re.split(r'[\s,]+',input_vecc)]
            if len(veca) != 3 or len(vecb) != 3 or len(vecc) != 3:
                raise IndexError
            if veca == [0,0,0] or vecb == [0,0,0] or vecc == [0,0,0]:
                print('零向量無法計算體積')
                break
            crossab = np.cross(veca,vecb)
            crossbc = np.cross(vecb,vecc)
            crossac = np.cross(veca,vecc)
            if np.array_equal(crossab,[0,0,0]) or np.array_equal(crossbc,[0,0,0]) or np.array_equal(crossac,[0,0,0]):
                print('兩向量平行，無法計算體積')
                break
            volume = np.absolute(np.dot(veca,crossbc))
            print('平行六面體體積為: ',volume)
            break
        except (IndexError,ValueError,TypeError):
            print('您輸入的向量有誤，請檢查向量是否包含三軸且使用,或空白鍵分隔')
            continue

    

#A點-反射點-B點(鏡面方程式or反射點)共兩組程式
#此求鏡面方程式
def mirror():
    while True:
        input_pointa = input('請輸入出發點座標: ')
        input_pointb = input('請輸入反射點座標: ')
        input_pointc = input('請輸入終點座標: ')
        try:
            pointa = [int(ipa) for ipa in re.split(r'[\s,]+',input_pointa)]
            pointb = [int(ipb) for ipb in re.split(r'[\s,]+',input_pointb)]
            pointc = [int(ipc) for ipc in re.split(r'[\s,]+',input_pointc)]
            if len(pointa) != 3 or len(pointb) != 3 or len(pointc) != 3:
                raise IndexError
            if pointa == pointb or pointb == pointc or pointa == pointc:
                print('有兩點相同，請檢查輸入值是否有誤')
                continue
            vecab = np.array([pointb[0]-pointa[0],pointb[1]-pointa[1],pointb[2]-pointa[2]])
            vecbc = np.array([pointc[0]-pointb[0],pointc[1]-pointb[1],pointc[2]-pointb[2]])
            distanceab = math.sqrt(((pointb[0]-pointa[0])**2)+((pointb[1]-pointa[1])**2)+((pointb[2]-pointa[2])**2))
            distancebc = math.sqrt(((pointc[0]-pointb[0])**2)+((pointc[1]-pointb[1])**2)+((pointc[2]-pointb[2])**2))
            if distanceab == 0 or distancebc == 0:
                print('兩點距離不能為0')
                continue
            lcm = math.lcm(int(distanceab),int(distancebc)) 
            m1 = lcm//distanceab
            m2 = lcm//distancebc
            mvecab = vecab*m1
            mvecbc = vecbc*m2
            normal_vec = mvecab+mvecbc
            if normal_vec[0] < 0:
                normal_vec = -normal_vec
            cfpv = math.gcd(normal_vec[0],normal_vec[1],normal_vec[2])
            npv = normal_vec//cfpv
            yplus = '+'
            zplus = '+'
            if npv[1]<0 :
                yplus = ''
            if npv[2]<0 :
                zplus = ''
            n = normal_vec[0]*pointb[0]+normal_vec[1]*pointb[1]+normal_vec[2]*pointb[2]
            print(str(normal_vec[0])+'x'+yplus+str(normal_vec[1])+'y'+zplus+str(normal_vec[2])+'z = '+str(n))
            break
            #這裡設計方程式 將反射點帶入檢查會不會在方程式上且在兩點間
            #if np.array_equal(vecab,vecbc):
            #    print('三點共線')
        except(IndexError,ValueError,TypeError):
            print('您輸入的值有誤，請檢查點和向量有無包含三軸值且使用,或空白鍵分隔')
            continue
        
#兩方程式求法向量
def two_eqation_n():
    while True:
        inputeq1 = input('請輸入方程式E1(係數若為1跟0仍需打出係數 且常數放右邊)\n: ')
        inputeq2 = input('請輸入方程式E2(係數若為1跟0仍需打出係數 且常數放右邊)\n: ')
        try:
            if 'x' not in inputeq1 or 'y' not in inputeq1 or 'z' not in inputeq1:
                raise IndexError
            elif 'x' not in inputeq2 or 'y' not in inputeq2 or 'z' not in inputeq2:
                raise IndexError
            else:
                pass
            eq1 =  re.split(r'[xyz]+',inputeq1)
            eq2 =  re.split(r'[xyz]+',inputeq2)
            vec1 = np.array([int(ie) for ie in eq1[:3]])
            vec2 = np.array([int(ie) for ie in eq2[:3]])
            if np.array_equal(vec1,vec2):
                print('兩方程式方向向量一致')
                break
            normal_vec = np.cross(vec1,vec2)
            if normal_vec[0] <0:
                normal_vec = normal_vec*-1
            print('兩方程式之法向量為: ',normal_vec)
        except (IndexError,ValueError,TypeError):
            print('您輸入的方程式有誤，請檢查後再次輸入\nE1: ',inputeq1,'\nE2: ',inputeq2)
            continue

#點面距
def distance_point_flat():
    while True:
        input_point = input('請輸入點座標(以,或空白分隔): ')
        input_line = input('請輸入平面一般式(係數若為1跟0仍需打出係數 且常數放左邊)\n: ')
        try:
            point = [int(ip) for ip in re.split(r'[\s,]+',input_point)]
            if len(point) != 3:
                raise IndexError
            line = re.split(r'[xyz=]+',input_line)
            coef = [int(il) for il in line[:4]]
            num = abs(point[0]*coef[0]+point[1]*coef[1]+point[2]*coef[2]+coef[3])
            den = math.sqrt(coef[0]**2+coef[1]**2+coef[2]**2)
            if den.is_integer():
                distance = num/den
                if distance.is_integer():
                    print(int(distance))
                else:
                    print(str(num)+'/'+str(int(den)))
            else:
                distance = str(num)+'/'+'√￣'+str(coef[0]**2+coef[1]**2+coef[2]**2)
                print(distance)
            break
        except (IndexError,ValueError,TypeError):
            print('您輸入的值有誤，請檢查後再次輸入\n點座標: ',input_point,'\n平面一般式: ',input_line)
            continue    
