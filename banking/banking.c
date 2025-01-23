#include <stdio.h>
#include <stdlib.h>

#define SUCCESS 0
#define ERR_INVALID_AMOUNT 100
#define ERR_OVERLIMIT 200
#define ERR_OVERDRAW 300

float LIMIT_DEPOSIT = 1000.0;
float LIMIT_WITHDRAWAL = 200.0;

float balance = 0;

char *complain(int err) {
  switch (err) {
  case SUCCESS:
    return "Success";
  case ERR_INVALID_AMOUNT:
    return "Invalid amount entered";
  case ERR_OVERLIMIT:
    return "Amount of transaction exceeds limit.";
  case ERR_OVERDRAW:
    return "Overdraft";
  default:
    return "Unknown code";
  }
}

int deposit(float amount) {
  if (amount < 0)
    return ERR_INVALID_AMOUNT;
  if (amount > LIMIT_DEPOSIT)
    return ERR_OVERLIMIT;
  else {
    balance += amount;
    return SUCCESS;
  }
}

int withdraw(float amount) {
  if (amount < 0)
    return ERR_INVALID_AMOUNT;
  if (amount > LIMIT_WITHDRAWAL)
    return ERR_OVERLIMIT;
  if (amount > balance)
    return ERR_OVERDRAW;
  else {
    balance -= amount;
    return SUCCESS;
  }
}

float getBalance() { return balance; }

int main(void) {

  int result = SUCCESS;
  char option;
  float amount;
  int running = 1;
  int ret;

  while (running) {
    printf("(D)eposit\n(W)ithdraw\n(B)alance\n(Q)uit\nOption: ");
    ret = scanf(" %c", &option);

    switch (option) {
    case 'q':
    case 'Q':
      printf("Thank you for banking today\n");
      printf("Balance: $%.2f\n", getBalance());
      running = 0;
      break;

    case 'b':
    case 'B':
      printf("Current balance: $%0.2f\n\n", getBalance());
      break;

    case 'd':
    case 'D':

      printf("Enter deposit amount: ");
      ret = scanf(" %f", &amount);
      result = deposit(amount);
      printf("result = %s\n\n", complain(result));
      break;

    case 'w':
    case 'W':
      printf("Enter withdrawal amount: ");
      ret = scanf(" %f", &amount);
      result = withdraw(amount);
      printf("result = %s\n\n", complain(result));
      break;
    default:
      break;
    }
  }

  return 0;
}
