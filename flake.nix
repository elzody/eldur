{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      python = pkgs.python3;
    in
    {
      devShells.${system}.default =
        pkgs.mkShell {
          packages = [
            python
            pkgs.uv
            pkgs.gtk4
	    pkgs.gobject-introspection
          ];

          # Keep uv from downloading its own CPython: that interpreter runs
          # under nix-ld's older glibc and can't load the GTK libs below.
          env.UV_PYTHON = "${python}/bin/python3";
          env.UV_PYTHON_DOWNLOADS = "never";
        };
    };
}
