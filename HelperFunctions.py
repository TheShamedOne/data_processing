
def get_info(df):
  """
  Get summary of pandas database
  """
  print(df.info())
  print(df.head().to_markdown(numalign='left',stralign='left'))

def remove_dollar(x):
  """
  Remove dollar sign from data
  """
  if type(x) != str:
    return x
  x = x.replace('$','')
  x = x.strip()
  return x

def add_dollar(x):
  """
  Add dollar sign to data
  """
  if type(x) != str:
    return x
  return '$ ' + x  

def remove_comma(x):
  """
  Remove comma from data
  """
  if type(x) != str:
    return x
  return x.replace(',','')

def remove_dash(x):
  """
  Remove dash from data
  """
  if type(x) != str:
    return x
  return x.replace('-','')

def remove_percent(x):
  """
  Remove percent sign from data
  """
  if type(x) != str:
    return x
  return x.replace('%','')

def remove_dot(x):
  """
  Remove dot/period from data
  """
  if type(x) != str:
    return x
  return x.replace('.', '')

def to_bool(x):
  """
  Turn 'ACTIVE' tags into True and 'INACTIVE' into false.
  """
  if x == 'ACTIVE':
    return 1
  else:
    return 0

def foo_to_unkNown(x):
  """
  Turn 'foo' tags into 'UNKNOWN'.
  """
  if type(x) != str:
    return x
  if x == 'foo':
    return 'UNKNOWN'
  return x

def unabbreviate_mill(x):
  """
  Take data represented in millions and 
  unabbreviate it. I.E. 3 million into
  3000000.
  """
  return x * 1000000

def comma_to_dot(x):
  """
  Turn commas into dots/periods
  """
  if not isinstance(x, str):
    return x
  return x.replace(',', '.')  

def fix_neg(x):
  """
  Remove space next to negative sign.
  """
  if not isinstance(x, str):
    return x
  return x.replace('- ', '-')