#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int ft_count(int value, int base)
{
    int res;

    res = 0;
    while (value)
    {
        value = value / base;
        res++;
    }
    return (res);
}

char    *ft_itoa_base(int value, int base)
{
    char *str;
    char *hexa;
    int count;

    if (!(hexa = (char*)malloc(sizeof(char) * 17)))
        return (NULL);
    hexa = "0123456789ABCDEF";
    count = ft_count(value, base);
    if (!(str = (char *)malloc(sizeof(char) * (count + 1))))
        return (NULL);
    str[count] = '\0';
    count--;
    while (value)
    {
        str[count] = hexa[value % base];
        count--;
        value = value / base;
    }
    return (str);
}

int main(int ac, const char **av)
{
	if (ac == 3)
	{
		printf("taille de value : %zu\n", ft_count(atoi(av[1]), atoi(av[2])));
		printf("itoa : %s\n", ft_itoa_base(atoi(av[1]), atoi(av[2])));
	}
	return (0);
}