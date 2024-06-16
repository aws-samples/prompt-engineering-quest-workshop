# Use this system prompts
system = """"
  In this environment you have access to a set of tools you can use to answer the user's question.
  You may call them like this:
  <function_calls>
      <invoke>
          <tool_name>$TOOL_NAME</tool_name>
          <parameters>
              <$PARAMETER_NAME>$PARAMETER_VALUE</$PARAMETER_NAME>
              ...
          </parameters>
      </invoke>
  </function_calls>
  Here are the tools available:
  <tools>
    <tool_description>
      <tool_name>mul</tool_name>
      <description>
        Multiplication is the operation of finding the product of two or more numbers by repeated addition or scaling.
      </description>
      <parameters>
        <parameter>
          <name>num1</name>
          <type>integer</type>
          <description>The first number to use in the operation</description>
        </parameter>
        <parameter>
          <name>num3</name>
          <type>integer</type>
          <description>The second number to use in the operation</description>
        </parameter>
      </parameters>
    </tool_description>
    <tool_description>
      <tool_name>sum</tool_name>
      <description>
        Addition is the operation of combining two or more numbers to find their sum or total.
      </description>
      <parameters>
        <parameter>
          <name>num1</name>
          <type>integer</type>
          <description>The first number to use in the operation</description>
        </parameter>
        <parameter>
          <name>num3</name>
          <type>integer</type>
          <description>The second number to use in the operation</description>
        </parameter>
      </parameters>
    </tool_description>
    <tool_description>
      <tool_name>sum</tool_name>
      <description>
        Subtraction is the operation of finding the difference between two numbers by taking one number away from the other.
      </description>
      <parameters>
        <parameter>
          <name>num1</name>
          <type>integer</type>
          <description>The first number to use in the operation</description>
        </parameter>
        <parameter>
          <name>num3</name>
          <type>integer</type>
          <description>The second number to use in the operation</description>
        </parameter>
      </parameters>
    </tool_description>
  </tools>
"""

# Set this stop_sequence to have Claude stop generating once it calls a function 
stop_sequences = ['</function_calls>']
