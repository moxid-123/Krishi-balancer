import sympy as sp
x1,x2,u=sp.symbols('x1 x2 u')
x1_dot=-x1+2*x1**3+x2+4*u
x2_dot=-x1-x2+2*u
def find_equilibrium_points():
    x1_eq=x1_dot.subs(u,0)
    x2_eq=x2_dot.subs(u,0)
    eq1=sp.Eq(x1_eq,0)
    eq2=sp.Eq(x2_eq,0)
    eq_points=sp.solve((eq1,eq2),x1,x2)
    return eq_points
eq_points=find_equilibrium_points()
print("Equilibrium Points:")
for i,point in enumerate(eq_points):
    print(f" Point {i + 1}:x1 = {point[0]}, x2 = {point[1]}")