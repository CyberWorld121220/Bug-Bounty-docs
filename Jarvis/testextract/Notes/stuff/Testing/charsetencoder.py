import urllib
def paramEncode(params="", charset="IBM037", encodeEqualSign=False,encodeAmpersand=False, urldecodeInput=True, urlencodeOutput=True):
    result = ""
    equalSign = "="
    ampersand = "&"
    if encodeEqualSign:
       equalSign = equalSign.encode(charset)
    if encodeAmpersand:
       ampersand = ampersand.encode(charset)
    params_list = params.split("&")
    for param_pair in params_list:
       param, value = param_pair.split("=")
       if urldecodeInput:
          param = urllib.unquote(param).decode('utf8')
          value = urllib.unquote(value).decode('utf8')
       param = param.encode(charset)
       value = value.encode(charset)
       if urlencodeOutput:
          param = urllib.quote_plus(param)
          value = urllib.quote_plus(value)
       if result:
          result += ampersand
       result += param + equalSign + value
    return result
print("Note: if there are more then one parameter , then put them one by one , = and & will remain same")
#a = input("Put the string to encode: ")
print("Encode charser=IBM037")
print paramEncode("x=on/demandware.store/Sites-vidaxl-ch-Site/de_CH/Account-SaveProfile")
