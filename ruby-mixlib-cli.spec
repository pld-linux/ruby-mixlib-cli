%define		gem_name	mixlib-cli
Summary:	Simple Ruby mix-in for CLI interfaces
Name:		ruby-%{gem_name}
Version:	1.3.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages
URL:		http://github.com/opscode/mixlib-cli
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	ef197d6bf95a73680fb0bf279c5f33ac
# Patch to silence mixlib-cli tests;
# see http://tickets.opscode.com/browse/MIXLIB-8
Patch0:		mixlib-cli-silence-tests.patch
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
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
%if %{with tests}
# need RSpec2
rspec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc NOTICE
%{ruby_vendorlibdir}/mixlib/cli.rb
%{ruby_vendorlibdir}/mixlib/cli

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif