#
# Conditional build:
%bcond_without	tests		# build without tests

%define		pkgname	mixlib-cli
Summary:	Simple Ruby mix-in for CLI interfaces
Name:		ruby-%{pkgname}
Version:	1.4.0
Release:	2
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	1d26beabb487df9661d521c717846922
# Patch to silence mixlib-cli tests;
# see http://tickets.opscode.com/browse/MIXLIB-8
Patch0:		mixlib-cli-silence-tests.patch
URL:		http://github.com/opscode/mixlib-cli
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-rake
BuildRequires:	ruby-rdoc
BuildRequires:	ruby-rspec
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple mix-in for CLI interfaces, including option parsing.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
rspec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc NOTICE
%{ruby_vendorlibdir}/mixlib/cli.rb
%{ruby_vendorlibdir}/mixlib/cli
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif
