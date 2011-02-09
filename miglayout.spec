Summary:	Versatile and flexible Swing and SWT layout manager
Name:		miglayout
Version:	3.7.4
Release:	1
License:	BSD-like
Group:		Development/Languages/Java
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ffc19c929d4047420857fd2ee6c4c1fb
URL:		http://www.miglayout.com/
Requires:	jre >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MiGLayout is a versatile and flexible Swing and SWT layout manager. It
uses string constraints or API type-checked constraints to format the
layout. Strings are both short to type and easy to understand.
MiGLayout can produce flowing, grid-based, absolute (with links),
grouped, and docking layouts. It was created to be to manually coded
layouts what Matisse/GroupLayout is to IDE-supported visual layouts.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install %{name}-%{version}-ideutil.jar $RPM_BUILD_ROOT%{_javadir}
install %{name}-%{version}-swing.jar $RPM_BUILD_ROOT%{_javadir}
install %{name}-%{version}-swt.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf %{name}-%{version}-ideutil.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ideutil.jar
ln -sf %{name}-%{version}-swing.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-swing.jar
ln -sf %{name}-%{version}-swt.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-swt.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
