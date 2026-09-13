class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # in this problem we have to iterate both part of the array, index and value, beacuse we have to return the index, but the value is important 
        hash = { }
        for i, v in enumerate(nums):
            findValue = target - v
            if findValue in hash:
                return [hash[findValue],i] # retornamos los dos indices, con has[findValue] le pasamos el valor para que nos retorne el indice, asi se retorna un indice en un hashmap, necesita que le mande el valor
            hash[v] = i # aqui digo que quiero ingresar el valor con el indice tal, por eso igualamos la incursion a la memoria del hashmap del valor que queremos agregar y lo igualamo al inide, le decimos, guardame este valor en este indice 