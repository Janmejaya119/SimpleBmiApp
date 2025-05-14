var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/bmi", (double weight, double height) =>
{
    double bmi = weight / (height * height);
    return Results.Ok(new { BMI = bmi, Category = GetBmiCategory(bmi) });
});

string GetBmiCategory(double bmi) => bmi switch
{
    < 18.5 => "Underweight",
    < 25.0 => "Normal weight",
    < 30.0 => "Overweight",
    _ => "Obese"
};

app.Run();
