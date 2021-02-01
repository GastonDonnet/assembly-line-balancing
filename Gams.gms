Sets
i Actividades a realizar / i1*i33 /

k Estaciones de trabajo / eta1*eta2, et1*et5 /
* eta#: Estaciones de apoyo
* et#: Estaciones principales

p Producto / P1*P5 /
* P1: Semi Acoplado: con frente
* P2: Semi Acoplado: con puerta trasera
* P3: Semi Acoplado: con puerta libro
* P4: Acoplado: con puerta trasera
* P5: Acoplado: con puerta libro
;

*Alias sirve para crear una copia del conjunto
Alias(i,ii)
Alias(k,kk)
;

Sets
precedencia(i,ii) Actividad i sucede a actividad ii (grafo de precedencias combinado) / i3.(i1), i4.(i2), i12.(i5, i11), i13.(i12, i9), i14.(i13), i15.(i12), i16.(i14, i15), i17.(i16), i18.(i17), i19.(i18), i20.(i21), i21.(i19), i22.(i21), i23.(i22), i24.(i3, i4, i8, i26, i30, i31), i25.(i6, i10, i24), i26.(i20, i23, i27), i29.(i7, i28), i30.(i19, i29), i31.(i19, i32, i33)    /
AApoyo(i) Actividades que deben realizarse en estaciones de apoyo / i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i27, i28, i29, i32, i33  /
APrincipal(i) Actividades que deben realizarse en estaciones principales / i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25, i26, i30, i31   /
EApoyo(k) Estaciones de apoyo / eta1*eta2 /
EPrincipal(k) Estaciones principales / et1*et5 /
;

Parameters
kObjetivo Estaciones a usar / 7 /
opReq(i) Operarios que requiere la actividad t / i1 1, i2 1, i3 1, i4 1, i5 1, i6 1, i7 1, i8 1, i9 1, i10 1, i11 2, i12 2, i13 2, i14 2, i15 2, i16 2, i17 2, i18 1, i19 1, i20 1, i21 1, i22 1, i23 1, i24 1, i25 1, i26 1, i27 1, i28 1, i29 1, i30 1, i31 1, i32 1, i33 1 /
opDisp Operarios disponibles / 9 /
;

Table
tiempo(i,p) Tiempo de operación de actividad i (minutos)
    P1      P2      P3      P4      P5
i1  014.60  014.60  014.60  021.60  021.60
i2  009.30  009.30  009.30  009.30  009.30
i3  017.50  017.50  017.50  029.70  029.70
i4  012.80  012.80  012.80  012.80  012.80
i5  015.10  015.10  015.10  025.80  025.80
i6  034.30  034.30  034.30  064.80  064.80
i7  006.90  006.90  006.90  006.90  006.90
i8  005.90  005.90  005.90  005.90  005.90
i9  005.50  005.50  005.50  005.50  005.50
i10 031.30  031.30  031.30  063.50  063.50
i11 061.40  061.40  061.40  070.60  070.60
i12 080.10  080.10  080.10  091.80  091.80
i13 014.60  014.60  014.60  019.80  019.80
i14 029.30  029.30  029.30  037.30  037.30
i15 047.00  047.00  047.00  055.80  055.80
i16 036.60  036.60  036.60  048.40  048.40
i17 005.80  005.80  005.80  005.80  005.80
i18 118.90  118.90  118.90  118.90  118.90
i19 043.10  043.10  043.10  050.10  050.10
i20 041.50  041.50  041.50  041.50  041.50
i21 027.80  027.80  027.80  034.20  034.20
i22 005.40  005.40  005.40  005.40  005.40
i23 027.90  027.90  027.90  042.00  042.00
i24 040.70  040.70  040.70  045.00  045.00
i25 050.40  050.40  050.40  079.80  079.80
i26 036.30  036.30  036.30  000.00  000.00
i27 022.40  022.40  022.40  000.00  000.00
i28 013.00  000.00  000.00  013.00  013.00
i29 030.70  000.00  000.00  030.70  030.70
i30 029.90  000.00  000.00  029.90  029.90
i31 000.00  059.60  051.00  059.60  059.60
i32 000.00  043.80  000.00  043.80  000.00
i33 000.00  000.00  058.50  000.00  058.50

;

Binary variables
X(i,k) Toma 1 si la actividad i es asignada a la estación de trabajo j. 0 en caso contrario.
;

Integer variables
opET(k) Numero de operarios asignados a estación de trabajo j
;

Positive variables
TCp(p) Tiempo de ciclo
TEp(k,p) Tiempo requerido por la estación de trabajo j para realizar actividades asignadas
TOp(k,p) Tiempo ocioso de la estación de trabajo j

TC Tiempo de ciclo
;

Free variable
z Función objetivo
;

Equations
R1 Restricción de realización de una
R2 Restricción de calculo de tiempo usado en una estación
R2b Restricción (No lineal) de calculo de tiempo usado en una estación con modificación de operarios
R3 Restricción de tiempo de ciclo
R4a Restricción de precedencias de actividades principales
R4b Restricción de precedencias de actividades de apoyo (Obliga a las actividades de apoyo a respetar su precedencia si o si dentro de la propia estación)
R5 Restricción de operarios disponibles
R6 Restricción de asignación de operario a estación
R7 Restricción de calculo de tiempo ocioso de una estación
R8 Restricción de calculo del TC máximo
R9 Obliga a las actividades principales a hacerse en estaciones principales
R10 Obliga a las actividades de apoyo a hacerse en estaciones de apoyo

FO1 Función objetivo: Minimizar sumas de tiempos de ciclo de cada producto
FO2 Función objetivo: Minimizar tiempo de ciclo maximo entre productos
FO3 Función objetivo: Minimizar suma de tiempos ociosos de ambos productos
FO4 Función objetivo (No lineal): Minimizar suma de indices de suavizacion
;

R1(i).. Sum(k, X(i,k)) =E= 1;
R2(k,p).. Sum(i, X(i,k)*tiempo(i,p)) =E= TEp(k,p);
R2b(k,p).. Sum(i, X(i,k)*tiempo(i,p)*opReq(i)/opET(k)) =E= TEp(k,p);
R3(k,p).. TEp(k,p) =L= TCp(p);
R4a(i,ii,k)$(precedencia(i,ii)).. X(i,k) =L= Sum(kk$(ord(kk)<=ord(k)),X(ii,kk));
R4b(i,ii,k)$(precedencia(i,ii) and AApoyo(i) and AApoyo(ii)).. X(i,k) =L= Sum(kk$(ord(kk)=ord(k)),X(ii,kk));
R5.. Sum(k, opET(k))=L=opDisp;
R6(k,i).. opET(k) =G= X(i,k)*opReq(i);
R7(k,p).. TOp(k,p) =E= TCp(p) - TEp(k,p);
R8(p).. TC =G= TCp(p);
R9(k)$(EApoyo(k)).. Sum(i$(APrincipal(i)), X(i,k)) =E= 0;
R10(k)$(EPrincipal(k)).. Sum(i$(AApoyo(i)), X(i,k)) =E= 0;

*Todas las estaciones deben tener al menos 1 operario
opET.lo(k) = 1;

*Funciones Objetivo
FO1.. z =E= Sum(p, TCp(p));
FO2.. z =E= TC;
FO3.. z =E= Sum((k,p), TOp(k,p));
FO4.. z =E= Sum(p,(Sum(k, (TCp(p)-TEp(k,p))**2))**(1/2));

*Opciones del programa
Options
optcr=0.00
optca=0.00
limrow = 99 
mip=cplex
sysout=on
;

**********************************************************************
** Funciones objetivos 
** Con restricción de tiempo de estación lineales
** Separando restricciones de precedencia de actividades de apoyo y actividades principales
**********************************************************************

*Minimiza Sum de TC
model M_FO1 / R1, R2, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO1 /;
solve M_FO1 minimizing z using mip;

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;
execute_unload 'M_FO1.gdx'

*Minimiza TC Máximo
model M_FO2 / R1, R2, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO2 /;
solve M_FO2 minimizing z using mip;
execute_unload 'M_FO2.gdx'

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;

*Minimiza Suma de TO
model M_FO3 / R1, R2, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO3/;
solve M_FO3 minimizing z using mip;

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;
execute_unload 'M_FO3.gdx'

*Minimiza Suma de Índices de Suavización
model M_FO4 / R1, R2, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO4/;
solve M_FO4 minimizing z using minlp;

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;
execute_unload 'M_FO4.gdx'

**********************************************************************
** Funciones objetivos 
** Con restricción de tiempo de estación no lineales
** Ignorando restricciones de precedencia de actividades de apoyo
**********************************************************************

*Minimiza Suma de TC
model M_FO1_OP / R1, R2b, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO1/;
solve M_FO1_OP minimizing z using minlp;

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;
execute_unload 'M_FO1_OP.gdx'

*Minimiza TC Máximo
model M_FO2_OP / R1, R2b, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO2 /;
solve M_FO2_OP minimizing z using minlp;

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;
execute_unload 'M_FO2_OP.gdx'

*Minimiza Suma de TO
model M_FO3_OP / R1, R2b, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO3/;
solve M_FO3_OP minimizing z using minlp;

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;
execute_unload 'M_FO3_OP.gdx'

*Minimiza Índice de suavización
model M_FO4_OP / R1, R2b, R3, R4a, R4b, R5, R6, R7, R8, R9, R10, FO4/;
solve M_FO4_OP minimizing z using minlp;

parameter EF Eficiencia de línea;
parameter IS Índice de suavización;
EF(p) = 100*Sum(i, tiempo(i, p))/(kObjetivo*TCp.l(p));
IS(p) = (Sum(k, (TCp.l(p)-TEp.l(k,p))**2))**(1/2);
display X.l, TEp.l, TCp.l, TOp.l, opET.l, TC.l, EF, IS, Z.l;
execute_unload 'M_FO4_OP.gdx'
