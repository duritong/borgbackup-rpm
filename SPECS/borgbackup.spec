Name: borgbackup
Version: 0.25.0
Release: 1

Summary: Deduplicating backup program with compression and authenticated encryption

License: BSD like
Group: File tools
Url: https://borgbackup.github.io/borgbackup/

Packager: mh <mh@immerda.ch>

Source: https://pypi.python.org/packages/source/%(c=%{name}; echo ${c:0:1})/%{name}/%{name}-%{version}.tar.gz
BuildRequires: openssl-devel, python3-devel, lz4-devel, libacl-devel
Requires: libacl, openssl, lz4, python3-msgpack

%description
BorgBackup (short: Borg) is a deduplicating backup program.
Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data.
The data deduplication technique used makes Borg suitable for daily backups since
only changes are stored.

The authenticated encryption technique makes it suitable for backups to not fully trusted targets.

%prep
%setup

%build
%py3_build

%install
%py3_install

%files
%doc LICENSE AUTHORS CHANGES.rst README.rst
%{_bindir}/borg
%{python3_sitearch}/*

%changelog
* Tue Sep 15 2015 mh <mh@immerda.ch> 0.25.0-1
- initial build for fedora
