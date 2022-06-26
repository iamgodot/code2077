# 编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。


def validIPAddress(self, queryIP: str) -> str:
    res = "Neither"

    if "." in queryIP:
        splitted = queryIP.split(".")
        if len(splitted) != 4:
            return res

        for part in splitted:
            try:
                if len(part) > 1 and part.startswith("0"):
                    break
                i = int(part)
                if i > 255:
                    break
            except Exception:
                break
        else:
            return "IPv4"
    elif ":" in queryIP:
        splitted = queryIP.split(":")
        if len(splitted) != 8:
            return res

        for x in splitted:
            hexdigits = "0123456789abcdefABCDEF"
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        else:
            return "IPv6"

    return res
