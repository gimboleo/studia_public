#include <stdio.h>
#include <string.h>
#include <assert.h>

typedef struct 
{
    char number[18];
    char checksum;

    char region[20];
    char country[20];
    char manufacturer[50];
    int year;
} Car;

void region(Car *car)
{
    char reg = car->number[0];
    if (reg >= 'A' && reg <= 'H') strcpy(car->region, "Africa");
    else if (reg >= 'J' && reg <= 'R') strcpy(car->region, "Asia");
    else if (reg >= 'S' && reg <= 'Z') strcpy(car->region, "Europe");
    else if (reg >= '1' && reg <= '5') strcpy(car->region, "North America");
    else if (reg >= '6' && reg <= '7') strcpy(car->region, "Oceania");
    else if (reg >= '8' && reg <= '9') strcpy(car->region, "South America");
    else strcpy(car->region, "Unknown");
}

void country(Car *car) 
{
    char country[2];
    for(int i = 0; i < 2; i++) country[i] = car->number[i];

    if (country[0] == 'A')
    {
        if (country[1] >= 'A' && country[1] <= 'H') strcpy(car->country, "South Africa");
        else if (country[1] >= 'J' && country[1] <= 'N') strcpy(car->country, "Cote d'Ivoire");
        else if (country[1] >= 'L' && country[1] <= 'R') strcpy(car->country, "Algeria");
    } 

    else if (country[0] == 'B')
    {
        if (country[1] >= 'A' && country[1] <= 'E') strcpy(car->country, "Angola");
        else if (country[1] >= 'F' && country[1] <= 'K') strcpy(car->country, "Kenya");
        else if (country[1] >= 'L' && country[1] <= 'R') strcpy(car->country, "Tanzania");
    } 

    else if (country[0] == 'C')
    {
        if (country[1] >= 'A' && country[1] <= 'E') strcpy(car->country, "Benin");
        else if (country[1] >= 'F' && country[1] <= 'K') strcpy(car->country, "Madagascar");
        else if (country[1] >= 'L' && country[1] <= 'R') strcpy(car->country, "Tunisia");
    }

    else if (country[0] == 'J') strcpy(car->country, "Japan");

    else if (country[0] == 'K')
    {
        if (country[1] >= 'A' && country[1] <= 'E') strcpy(car->country, "Sri Lanka");
        else if (country[1] >= 'F' && country[1] <= 'K') strcpy(car->country, "Israel");
        else if (country[1] >= 'L' && country[1] <= 'R') strcpy(car->country, "South Korea");
        else if (country[1] == 'S') strcpy(car->country, "Jordan");
        else if ((country[1] >= 'T' && country[1] <= 'Z') || country[1] >= '0' && country[1] <= '9') strcpy(car->country, "Kazahstan");
    }

    else if (country[0] == 'L') strcpy(car->country, "China (Mainland)");

    else if (country[0] == 'S')
    {
        if (country[1] >= 'A' && country[1] <= 'M') strcpy(car->country, "United Kingdom");
        else if (country[1] >= 'N' && country[1] <= 'T') strcpy(car->country, "Germany (FKA East)");
        else if (country[1] >= 'U' && country[1] <= 'Z') strcpy(car->country, "Poland");
        else if (country[1] >= '1' && country[1] <= '4') strcpy(car->country, "Latvia");
    }

    else if (country[0] == 'T')
    {
        if (country[1] >= 'A' && country[1] <= 'H') strcpy(car->country, "Switzerland");
        else if (country[1] >= 'J' && country[1] <= 'P') strcpy(car->country, "Czech Republic");
        else if (country[1] >= 'R' && country[1] <= 'V') strcpy(car->country, "Hungary");
        else if ((country[1] >= 'W' && country[1] <= 'Z') || country[1] == '1') strcpy(car->country, "Portugal");
    }

    else if (country[0] == 'U')
    {
        if (country[1] >= 'H' && country[1] <= 'M') strcpy(car->country, "Denmark");
        else if (country[1] >= 'N' && country[1] <= 'T') strcpy(car->country, "Ireland");
        else if (country[1] >= 'U' && country[1] <= 'Z') strcpy(car->country, "Romania");
        else if (country[1] >= '5' && country[1] <= '7') strcpy(car->country, "Slovakia");
    }

    else if (country[0] == 'W') strcpy(car->country, "Germany (FKA West)");

    else if (country[0] == '1' || country[0] == '4' || country[0] == '5') strcpy(car->country, "United States");

    else if (country[0] == '2') strcpy(car->country, "Canada");

    else if (country[0] == '6') strcpy(car->country, "Australia");

    else strcpy(car->country, "Unknown");
}

void manufacturer(Car *car)
{
    char man[4];
    for(int i = 0; i < 3; i++) man[i] = car->number[i];
    man[3] = '\0';

    if (!strcmp(man, "5YJ") || !strcmp(man, "LRW")) strcpy(car->manufacturer, "Tesla");
    else if (!strcmp(man, "WP0") || !strcmp(man, "WP1")) strcpy(car->manufacturer, "Porsche");
    else if (!strcmp(man, "AAV") || !strcmp(man, "PPV") || !strcmp(man, "WVG") || !strcmp(man, "WVW") || !strcmp(man, "WV1") || !strcmp(man, "WV2") || !strcmp(man, "1VW") || !strcmp(man, "3VW") || !strcmp(man, "8AW") || !strcmp(man, "9BW")) strcpy(car->manufacturer, "Volkswagen");
    else if (!strcmp(man, "WME")) strcpy(car->manufacturer, "Smart");
    else if (!strcmp(man, "MMR") || !strcmp(man, "PLP") || !strcmp(man, "4S3") || !strcmp(man, "4S4")) strcpy(car->manufacturer, "Subaru");
    else if (!strcmp(man, "TRU") || !strcmp(man, "WAU") || !strcmp(man, "99A")) strcpy(car->manufacturer, "Audi");
    else if (!strcmp(man, "VF7") || !strcmp(man, "VS7") || !strcmp(man, "8BC") || !strcmp(man, "935")) strcpy(car->manufacturer, "Citroen");
    else if (!strcmp(man, "JF5") || !strcmp(man, "1GM") || !strcmp(man, "2G2") || !strcmp(man, "6G2")) strcpy(car->manufacturer, "Pontiac");
    else if (!strcmp(man, "PL1")) strcpy(car->manufacturer, "Proton");
    else if (!strcmp(man, "ZHW")) strcpy(car->manufacturer, "Lamborghini");
    else strcpy(car->manufacturer, "Unknown");
}

void year(Car *car)
{
    char yr = car->number[9];
    if (yr >= 'A' && yr <= 'H') car->year = yr - 'A' + 2010;
    else if (yr >= 'J' && yr <= 'N') car->year = yr - 'A' + 2010 - 1;
    else if (yr == 'R') car->year = 2024;
    else if (yr >= 'S' && yr <= 'T') car->year = yr - 'A' + 2010 - 3;
    else if (yr >= 'V' && yr <= 'Y') car->year = yr - 'A' + 2010 - 4;
    else if (yr >= '1' && yr <= '9') car->year = yr - '1' + 2031;
    else car->year = 0;
}

Car decodeVin(char vin[]) 
{
    Car samochod;
    Car *pointer;
    pointer = &samochod;

    strcpy(samochod.number, vin);
    region(pointer);
    country(pointer);
    manufacturer(pointer);
    year(pointer);
    printf("%s\n", samochod.number);
    printf("%s\n", samochod.region);
    printf("%s\n", samochod.country);
    printf("%s\n", samochod.manufacturer);
    printf("%d\n", samochod.year);

    printf("\n");
    return samochod;
}

int main() 
{
    char autko[] = "1GMDX03E8VD266902";         //1997/2027 Pontiac (USA)
    Car x =decodeVin(autko);

    char autko2[] = "WP0AD29967S546242";        //2007/2037 Porsche (West Germany)
    Car y = decodeVin(autko2);

    char autko3[] = "3VWBC81H9SM110870";         //1995/2025 Volkswagen (Mexico)        //Brak meksyku w bazie
    Car z = decodeVin(autko3);

    assert(x.year == 2027);
    assert(!strcmp(x.manufacturer, "Pontiac"));

    assert(!strcmp(y.country, "Germany (FKA West)"));

    assert(!strcmp(z.country, "Unknown"));
    assert(!strcmp(z.region, "North America"));

    return 0;
}
