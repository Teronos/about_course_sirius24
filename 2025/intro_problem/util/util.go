package util

type TaskManager interface{
    ValidateLengthString(s string, n int) (bool, string)
    ValidateLengthInteger(s int, n int) (bool, string)
    Reverse(s string) string
    CountElement(s string, b rune) int
}

type CaseSolver struct {
    taskManager TaskManager
}

func (t *CaseSolver) ValidateLengthInteger(s int, n int) (bool, string){
    for s > 0{
        n--
        s/=10
    }

    if n > 0{
        return false, "number has less digits than n"
    }

    if n < 0{
        return false, "number has more digits than n"
    }

    return true, "number contains n digits"
}

func (t *CaseSolver) ValidateLengthString(s string, n int) (bool, string){
    realSize := len(s)

    if n > realSize{
        return false, "string length is less than n"
    }

    if n < realSize{
        return false, "string length is bigger than n"
    }

    return true, "string length is equal to n"
}

func (t *CaseSolver) Reverse(s string) string{
    runes := []rune(s)                                                                     
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func(t *CaseSolver) CountElement(s string, b rune) int{
    counter := 0
    for _, char := range s{
        if char == b{
            counter++
        }
    }

    return counter
}
