import numpy as np

class Simplex:
	def __init__(self, c, A, b, opt_type='max'):
		'''
		c : coefficient of the objective function (list or array)
		A : constraint matrix (left)
		b : constraint vector (vector >= 0)
		opt_type = 'max' or 'min'		
		'''
		
		self.c = np.array(c, dtype=float)
		self.A = np.array(A, dtype=float)
		self.b = np.array(b, dtype=float)
		self.opt_type = opt_type.lower()
		
		# If minimization, we transform in maximization min c.x <=> max -c.x
		
		if self.opt_type == 'min':
			self.c = -self.c
			
		self.nb_variable = len(self.c)
		self.nb_constraint = len(self.b)
		self.table = None
		
	def build_table(self):
		'''
		To create the table init to simplex with deviation variable (in french variable d'écart')
		'''
		# The identity matrix to deviation variable 
		
		I = np.eye(self.nb_constraint)
		
		# Top row (constaint + deviation variable + vector b)
		top = np.hstack((self.A, I, self.b.reshape(-1,1)))
		
		# Bottom row (objective function : -c for maximization, 0 for deviation, 0 for Z)
		bottom = np.hstack((-self.c, np.zeros(self.nb_constraint + 1)))
		self.table = np.vstack((top, bottom))
		
	def search_pivot(self):
				'''
				Find cols and rows in table
				'''
				# The end rows contains the reduces costs
				end_rows = self.table[-1, :-1]
				
				# Stop condition (Maximization) : every coefficient have to be >= 0
				if np.all(end_rows >= 0):
					return None, None
					
				# Cols pivot : the reduce costs more negative
				col_pivot = np.argmin(end_rows)
				
				# Rows pivot : test to report(b_i / A_ij for A_ij > 0)
				report = []
				for i in range(self.nb_constraint):
					val_inter = self.table[i, col_pivot]
					
					if val_inter > 0:
						report.append(self.table[i, -1] / val_inter)
					else :
						report.append(np.inf) # ignore if <= 0
						
				lig_pivot = np.argmin(report)
				
				if report[lig_pivot] == np.inf:
				 	raise ValueError("Le problème n'est pas borné (solution infinie).")
				return lig_pivot, col_pivot
				
	def pivoter(self, lig, col):
				'''
				To do the operation to pivot Gauss
				'''
				# Divide the rows pivot to have '1'
				self.table[lig] /= self.table[lig, col]
				
				# Cancel the other element to cols pivot
				for i in range(len(self.table)):
					if i != lig:
						self.table[i] -= self.table[i, col] * self.table[lig]
						
	def solve(self):
				'''
				To launch the simplex algorithm
				'''
				self.build_table()
				
				while True:
					lig, col = self.search_pivot()
					if lig is None : # Not reduces costs => optimun affected
						break
					self.pivoter(lig, col)
					
				# Extract the result
				sol = np.zeros(self.nb_variable)
				for j in range(self.nb_variable):
					column = self.table[:-1, j]
					# If column is basic (an alone 1 and other 0)
					if np.sum(column == 1) == 1 and np.sum(column == 0)== self.nb_constraint -1 :
						lig_index = np.where(column==1) [0][0]
						sol[j] = self.table[lig_index, -1]
				val_optimum = self.table[-1, -1]
								
				return sol, val_optimum
				
# --- EXEMPLES D'UTILISATION ---
if __name__ == "__main__":
    
    # ----------------------------------------------------
    # EXEMPLE 1 : MAXIMISATION
    # Maximiser Z = 3x1 + 2x2
    # Sous contraintes :
    # 2x1 + 1x2 <= 18
    # 2x1 + 3x2 <= 42
    # 3x1 + 1x2 <= 24
    # ----------------------------------------------------
    print("--- TEST MAXIMISATION ---")
    c_max = [450, 800]
    A_max = [
        [1.5, 2],
        [0.5, 0.75],
        [2, 3],
        [-1, 0],
        [0, -1],
        [1, 0],
        [0, 1]
    ]
    b_max = [250, 100, 327, -42, -53, 100, 100]

    solveur_max = Simplex(c_max, A_max, b_max, opt_type='max')
    sol_max, z_max = solveur_max.solve()
    print(f"Variables [x1, x2] optimales : {sol_max}")
    print(f"Valeur maximale de Z : {z_max}\n")


    # ----------------------------------------------------
    # EXEMPLE 2 : MINIMISATION
    # Minimiser Z = -2x1 - 5x2  (équivaut à Maximiser 2x1 + 5x2)
    # Sous contraintes :
    # 1x1 <= 4
    # 1x2 <= 6
    # 1x1 + 1x2 <= 8
    # ----------------------------------------------------
    print("--- TEST MINIMISATION ---")
    c_min = [-20, -40]
    A_min = [
        [2, 1],
        [1, 1],
        [1, 3]
    ]
    b_min = [16, 12, 18]

    solveur_min = Simplex(c_min, A_min, b_min, opt_type='min')
    sol_min, z_min = solveur_min.solve()
    print(f"Variables [x1, x2] optimales : {sol_min}")
    print(f"Valeur minimale de Z : {z_min}")