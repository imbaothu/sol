"""
CSCI204 Stack lab

Problem 1: infix parenthesized to a postfix expression.

Problem 2: evaluate a postfix expression.

Revised: Annie Ross, Feb 2022
"""

from stack import MyStack

class Infix2postfix:

  def __init__( self ):
    """
    Initalize the stack
    """
    self._stack = MyStack()

  def translate( self, expression ):
     output = ""  # Initialize the output variable
     self._clear_stack()    # prepare the stack

    # Split the expression into tokens based on whitespace
     tokens = expression.split()

     for token in tokens:
        # if value, put directly into output
        if self._is_variable(token):
            output = output + token + " "
        # if left paren, put on stack
        elif self._is_left_parens(token):
            self._stack.push(token)
        # if right paren, handle matches
        elif self._is_right_parens(token):
            output = output + self._handle_right_parens()
        # if operator, handle precedence
        elif self._is_op(token): 
            output = output + self._handle_standard_op(token)
        else:
            raise IllegalExpressionException(token)

     output = output + self._empty_stack()
     return output.strip()






  # ... existing code ...

  def evaluate_expression(self, expression):
    tokens = expression.split()
    for token in tokens:
        if self._is_variable(token):
            self._stack.push(token)
        elif self._is_op(token):
            right = self._stack.pop()
            left = self._stack.pop()
            result = self._do_op(token, left, right)
            self._stack.push(result)
    return self._stack.pop()

# ... rest of the code ...

  def _handle_right_parens( self ):
    """
    If we see a closing parenthesis ')', pop all items on the stack
    until the opening parenthesis '('.

    Parameters: none
    Return:
      string; representing all popped operators before matching left paren.
    Exceptions:
      raises ParensMismatchException if right paren has no left paren.
    """

    pops = ""
    while ( not self._stack.is_empty()) and (not self._stack.top() == '(' ):
        pops = pops + self._stack.pop() + ' '
    if self._stack.is_empty(): # missing the left parens
        raise ParensMismatchException()
    self._stack.pop() # the '('

    return pops

  def _clear_stack( self ):
    """
    Clears stack of all contents.
    
    Depending on how the stack is implemented, we can use different
    method.

    Parameters: none.
    Return: none.
    """
    while not self._stack.is_empty():
        self._stack.pop()
      
  def _is_variable( self, token ):
    """ Returns if the the given token a variable (as opposed to an operator
    or parenthesis)? We definte varible to be numeric.
    
    Parameters:
      token; string; string to evaluate.
    Return:
      True or False depending on if token is a variable. """

    # here we assume all operands are numeric
    return token.isnumeric()

  def _is_op( self, token ):
    """ Check if given token an operator. Supported operators + * - /.
    Parameters:
      token; string.
    Return:
      boolean depending on if token is a supported operator. """

    # we only support these four operations for now
    return token == '+' or token == '-' or token == '*' or token == '/'

  def _is_left_parens( self, token ):
    """ Check if token is a left parenthesis.
    Parameters:
      token; string.
    Return:
      boolean depending on if token is a left parenthesis. 
    """

    return token == '('

  def _is_right_parens( self, token ):
    """ Check if token is a right parenthesis.
    Parameters:
      token; string.
    Return:
      boolean depending on if token is a right parenthesis. 
    """

    return token == ')'

  def _handle_standard_op( self, op ):
    """ Pops all operators of the same or greater precedence of the provided
operator from the stack and pushes the given operator. 
    Parameters:
      op; string; a supported operator to compare to.
    Return:
      string representing all popped same or greater precedence operators.
    """

    pops = self._pop_higher_precedence_ops( op )
    self._stack.push( op )

    return pops

  def _pop_higher_precedence_ops( self, op ):
    """ Pops operators that have precedence >= op. 
   
    Parameters:
      op; string; a supported operator to compare to.
    Return:
      string representing all popped same or greater precedence operators.
    """
    pops = ""
    while ( not self._stack.is_empty() ) and \
          self._top_has_higher_precedence( op ):
        pops = pops + self._stack.pop() + ' '

    return pops

  def _top_has_higher_precedence( self, op ):
    """ Does the operator on the stack top have precedence greater than
    or equal to the given operator? Convert precedences into numbers
    to make this easy. Multiplicative operators (* /) are assigned 1,
    additive operators (+ -) are assigned 0. 
    
    Parameters:
      op; string; a supported operator to compare to.
    Return:
      boolean; True if operator at stack top has greater precedance than op; False otherwise.

    """

    top = self._stack.top()
    op_group = 0 
    top_group = 0 

    if op == '*' or op == '/':
        op_group = 1
    elif op == '(':
        op_group = 2

    if top == '*' or top == '/':
        top_group = 1
    elif top == '(':
        top_group = -1

    return top_group >= op_group

  def _empty_stack( self ):
    """ 
    Empties the stack while collecting each element as it is removed. 

    Parameters: none.
    Return:
      string; representing all popped contents of stack.
    """

    pops = ""
    while not self._stack.is_empty():
        if self._stack.top() == '(': # missing right parens
            raise ParensMismatchException()
        pops = pops + self._stack.pop() + ' '

    return pops

  def _do_op( self, op, left, right ):
    """
    Computing the arithmetic expression 'left' op 'right'.

    Paramters:
      op; string; representing a supported operationr (+,-,/,*).
      left; string; representing the int left operand.
      right; string; value representing the intright operand.
    Return
      string; representing completed operation.

    E.g., _do_op('-','5','2') returns '3'
    """

    # convert string to int
    lvalue = int(left)
    rvalue = int(right)

    # do the operation
    if op == '+':   # do addition
        value = lvalue + rvalue
    elif op == '-': # do subtraction
        value = lvalue - rvalue
    elif op == '*': # do multiplication
        value = lvalue * rvalue
    elif op == '/': # do int division
        value = lvalue // rvalue
    else:
        raise IllegalExpressionException(op)

    # convert back to string
    svalue = str(value)

    return svalue

class ParensMismatchException( Exception ):
  def __init__( self ):
    pass

  def __str__( self ):
    return 'Parenthesis mismatch exception'

class IllegalExpressionException( Exception ):
  def __init__( self, op='' ):
    super().__init__()
    self.op = op

  def __str__( self ):
    return 'Illegal expression exception: \''+str(self.op)+'\''


