#
# spec file for package aws-regions
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define python python
%{?sle15_python_module_pythons}

Name:           python-aws-regions
Version:        0.2.0
Release:        0
Summary:        API for retrieving the most up-to-date AWS region list
License:        MIT
URL:            https://github.com/SUSE-Enceladus/aws-regions
Source:         https://files.pythonhosted.org/packages/source/a/aws-regions/aws-regions-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module vcrpy}
BuildRequires:  %{python_module pytest}
Requires:       python-requests
%python_subpackages

%description

%prep
%autosetup -n aws-regions-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.md README.md
%{python_sitelib}/*

%changelog


