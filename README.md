<p align="center"><a href="#readme"><img src="https://gh.kaos.st/anicorn.png"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/cain/ci"><img src="https://kaos.sh/w/cain/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#contributing">Contributing</a> • <a href="#license">License</a></p>

<br/>

`Anicorn` it's a simple utility for starting/restarting [Unicorn HTTP server](https://bogomips.org/unicorn/) while using init system.

**Attention!** If you use Anicorn with systemd, you should set [`KillMode`](https://www.freedesktop.org/software/systemd/man/systemd.kill.html#KillMode=) to `process` (`control-group` by default).

### Installation

#### From [ESSENTIAL KAOS Public Repository](https://yum.kaos.st)

```bash
sudo yum install -y https://yum.kaos.st/get/$(uname -r).rpm
sudo yum install anicorn
```

#### Using Makefile and Git

```bash
git clone https://kaos.sh/anicorn.git
cd anicorn
sudo make install
```

### Usage

```
Usage: anicorn unicorn-conf

Params

  unicorn-conf  Path to Unicorn configuration file

Examples

  anicorn /srv/projects/example/current/config/unicorn.rb
  Run Unicorn with Anicorn

```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/cain/ci.svg?branch=master)](https://kaos.sh/w/cain/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/cain/ci.svg?branch=master)](https://kaos.sh/w/cain/ci?query=branch:develop) |

### Contributing

Before contributing to this project please read our [Contributing Guidelines](https://github.com/essentialkaos/contributing-guidelines#contributing-guidelines).

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
