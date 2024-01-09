using System;

class Program
{

 
    static void Main()
    {

        int userInput;

        if (int.TryParse(Console.ReadLine(), out userInput))
        {
            Program programInstance = new Program();
            programInstance.MyProperty = userInput;
            programInstance.RunCalculationWithInput(userInput);
           
        }

    }
    public int MyProperty { get; set; }
    public void RunCalculationWithInput(int userInput)
    {
        int iterationCount;
        MyProperty = userInput;
        for (iterationCount = 1; ; iterationCount++)
        {         

            MyProperty = MyProperty - iterationCount;


            if (MyProperty <= 0 && iterationCount % 2 == 1)
            {
                
                Console.WriteLine((-MyProperty + 1)  +"/" + (iterationCount + MyProperty));
                break;
            }
            if (MyProperty <= 0)
            {

                Console.WriteLine((iterationCount + MyProperty) + "/" + (-MyProperty + 1));
                break;
            }
        }
    }
}