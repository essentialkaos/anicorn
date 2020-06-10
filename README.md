<p align="center"><a href="#readme"><img src="https://gh.kaos.st/anicorn.png"/></a></p>

<p align="center">
  <a href="https://travis-ci.org/essentialkaos/anicorn"><img src="https://travis-ci.org/essentialkaos/anicorn.svg"></a>
  <a href="https://essentialkaos.com/ekol"><img src="https://gh.kaos.st/ekol.svg"></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#contributing">Contributing</a> • <a href="#license">License</a></p>

<br/>

`Anicorn` it's a simple utility for starting/restarting [Unicorn HTTP server](https://bogomips.org/unicorn/) while using init system.

**Attention!** If you use Anicorn with systemd, you should set [`KillMode`](https://www.freedesktop.org/software/systemd/man/systemd.kill.html#KillMode=) to `process` (`control-group` by default).

### Installation

#### From ESSENTIAL KAOS Public repository

```
sudo yum install -y https://yum.kaos.st/get/$(uname -r).rpm
sudo yum install anicorn
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
| `master` | [![Build Status](https://travis-ci.org/essentialkaos/anicorn.svg?branch=master)](https://travis-ci.org/essentialkaos/anicorn) |
| `develop` | [![Build Status](https://travis-ci.org/essentialkaos/anicorn.svg?branch=develop)](https://travis-ci.org/essentialkaos/anicorn) |

### Contributing

Before contributing to this project please read our [Contributing Guidelines](https://github.com/essentialkaos/contributing-guidelines#contributing-guidelines).

### License

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
