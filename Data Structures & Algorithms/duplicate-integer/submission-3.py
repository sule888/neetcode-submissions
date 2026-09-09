class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # el hashmap es una estrutura que me permite guardar los valores que ya haya visto y aceder a ello con facilidad
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False  


## sabiendo que el set elimina duplicados otro aproah es solo conpaar la logitud de lo dos: return len(set(nums) < len(nums)) ------ longitud de el set del array de numeros menor a longitud del array numeros, si es menor significa que efetivamente hay dupliados y da true, si no es que on igules, no puede er maor por eso es el signo menor a, asi que da false y no hay dupliacdos