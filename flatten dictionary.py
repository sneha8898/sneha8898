def flattenDictionaryHelper(nestedDict, flattenedDic, currentKey):
    for key in nestedDict.keys():
        if type(nestedDict[key]) == int:
            flattenedDic[(currentKey+"."+key).strip(".")] = nestedDict[key]
        else:
            flattenedDic = flattenDictionaryHelper(nestedDict[key], flattenedDic, (currentKey+"."+key).strip('.'))
    
    return flattenedDic

def flattenDictionary(nestedDic):
    return flattenDictionaryHelper(nestedDic, dict(), "")

def main():
    nestedDictionary = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

    flattenedDictionary = flattenDictionary(nestedDictionary)
    print(flattenedDictionary)

if __name__ == "__main__":
    main()
