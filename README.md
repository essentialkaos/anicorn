<p align="center"><a href="#readme"><img src=".github/images/card.png"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/cain/ci"><img src="https://kaos.sh/w/cain/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src=".github/images/license.svg"/></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#ci-status">CI Status</a> • <a href="#contributing">Contributing</a> • <a href="#license">License</a></p>

<br/>

`Anicorn` it's a simple utility for starting/restarting [Unicorn HTTP server](https://bogomips.org/unicorn/) while using init system.

> [!IMPORTANT]  
> If you use Anicorn with systemd, you should set [`KillMode`](https://www.freedesktop.org/software/systemd/man/systemd.kill.html#KillMode=) to `process` (`control-group` _by default_).

### Installation

#### From [ESSENTIAL KAOS Public Repository](https://kaos.sh/kaos-repo)

```bash
sudo yum install -y https://pkgs.kaos.st/kaos-repo-latest.el$(grep 'CPE_NAME' /etc/os-release | tr -d '"' | cut -d':' -f5).noarch.rpm
sudo yum install anicorn
```

#### Using Makefile and Git

```bash
git clone https://kaos.sh/anicorn.git
cd anicorn
sudo make install
```

### Usage

<img src=".github/images/usage.svg"/>

### CI Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/cain/ci.svg?branch=master)](https://kaos.sh/w/cain/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/cain/ci.svg?branch=master)](https://kaos.sh/w/cain/ci?query=branch:develop) |

### Contributing

Before contributing to this project please read our [Contributing Guidelines](https://github.com/essentialkaos/contributing-guidelines#contributing-guidelines).

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
