class solution:
    def solve(self):
        query = "SELECT c.code AS competency_code, CASE WHEN EXISTS (SELECT 1 FROM program_discipline pd JOIN discipline_competency dc ON pd.discipline_id = dc.discipline_id WHERE pd.program_id = p.program_id AND dc.competency_id = c.competency_id) THEN 1 ELSE 0 END AS is_covered FROM program p JOIN role_competency rc ON p.role_id = rc.role_id JOIN competency c ON rc.competency_id = c.competency_id WHERE p.code = $program_code ORDER BY c.code"
        print(query)