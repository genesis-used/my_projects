def rot13(message):
    final = ''
    start_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','A',
    'B','C','D','E','F','G','H','I','J','K','L','M']
    de_list = ['n','o','p','q','r','s','t','u','v','w','x','y','z','N','O',
    'P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for letter in message:
        
        if letter in start_list:
            x = start_list.index(letter)
            final += de_list[x]
        
        elif letter in de_list:
            x = de_list.index(letter)
            final += start_list[x]
        
        else:
            final += letter
    
    return final