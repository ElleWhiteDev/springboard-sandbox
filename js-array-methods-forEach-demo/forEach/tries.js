const bills = [22, 53, 75, 32];
let monthlyBudget = 0;

bills.forEach(function (bill) {
    monthlyBudget += bill;  
})
console.log(monthlyBudget);