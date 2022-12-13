#include <iostream>



double* RandomVector(int seed, int x, int y)
{
    int v = (seed - y + x + x) % 4;

    double* res = new double[2];

    switch (v)
    {
    case 0:
        res[0] = double(1.0f); res[1] = double(0.0f);
        return res;
        break;
    case 1:
        res[0] = double(0.0f); res[1] = double(1.0f);
        return res;
        break;
    case 2:
        res[0] = double(-1.0f); res[1] = double(0.0f);
        return res;
        break;
    default:
        res[0] = double(0.0f); res[1] = double(-1.0f);
        return res;
        break;
    }
}

double DotProduct(double* a, double* b)
{
    return a[0] * b[0] + a[1] * b[1];
}

double QunticCurve(double t)
{
    return t * t * t * (t * (t * 6 - 15) + 10);
}

double Lerp(double a, double b, float t)
{
    return a + (b - a) * t;
}

double DotValue(double LT, double RT, double LB, double RB, float x, float y)
{
    x = QunticCurve(x);
    y = QunticCurve(y);

    double top = Lerp(LT, RT, x);
    double bot = Lerp(LB, RB, x);
    double tot = Lerp(top, bot, y);

    return tot;

}

double* GenerateChunk(int seed, double left, double top, double size)
{   
    double noise[16 * 16];

    double* LTrandVec = RandomVector(seed, left, top);
    double* RTrandVec = RandomVector(seed, left + 1.0, top);
    double* LBrandVec = RandomVector(seed, left, top - 1.0);
    double* RBrandVec = RandomVector(seed, left + 1.0, top - 1.0);

    for (int x = left; x <= left + size - 1; x++) {

        for (int y = top; y >= top - size + 1; y--) {

            double LTVec[2] = { (x - left) / size , (y - top) / size };
            double RTVec[2] = { (x - (left + size)) / size, (y - top) / size };
            double LBVec[2] = { (x - left) / size, (y - (top - size)) / size };
            double RBVec[2] = { (x - (left + size)) / size, (y - (top - size)) / size };
       

            double LT = DotProduct(LTrandVec, LTVec);
            double RT = DotProduct(RTrandVec, RTVec);
            double LB = DotProduct(LBrandVec, LBVec);
            double RB = DotProduct(RBrandVec, RBVec);




            float locX = (x - left) / size;
            float locY = (top - y) / size;

            int i = (x - left) * size + (top - y);
            if (i == 152) {
                //std::cout << LT << " " << RT << " " << LB << " " << RB << " " << DotValue(LT, RT, LB, RB, locX, locY);
            }

            noise[i] = DotValue(LT, RT, LB, RB, locX, locY);

        }
    }
    return noise;
}






int main()
{
    int seed = 1232;
    double left = 1.0;
    double top = 2.0;
    double size = 16.0;
    int k = 0;
    int c = 0;
    double* noise = GenerateChunk(seed, left, top, size);
    //for (int i = 0; i < 16 * 16; i++)
    //{
        //if (i == 152) {
            //std::cout << i << " " << noise[i] << "\n";
        //}

    //}
            
            std::cout << noise[152] << "\n";
}