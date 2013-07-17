python-ctrldaemon
=================

*Service command wrapper for Python.*

Use
-------------------------------

**Create object**

```python
from ctrldaemon import ControlDaemon
obj = ControlDaemon("service") # Example "httpd" (Apache)
```

**Start service**

```python
from ctrldaemon import ControlDaemon
obj = ControlDaemon("service") # Example "httpd" (Apache)
obj.start()
```

**Stop service**

```python
from ctrldaemon import ControlDaemon
obj = ControlDaemon("service") # Example "httpd" (Apache)
obj.stop()
```

**Restart service**

```python
from ctrldaemon import ControlDaemon
obj = ControlDaemon("service") # Example "httpd" (Apache)
obj.restart()
```

**Memory**

```python
from ctrldaemon import ControlDaemon
obj = ControlDaemon("service") # Example "httpd" (Apache)
obj.get_memory_usage()
```
