%global packname  RSVGTipsDevice
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0_4
Release:          3
Summary:          An R SVG graphics device with dynamic tips and hyperlinks
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
A graphics device for R that uses the w3.org xml standard for Scalable
Vector Graphics.  This version supports tooltips with 1 to 3 lines,
hyperlinks, and line styles.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/serverconfig


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_4-1
+ Revision: 777719
- Import R-RSVGTipsDevice
- Import R-RSVGTipsDevice

